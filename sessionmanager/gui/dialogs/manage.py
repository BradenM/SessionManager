# Program: Session Manager
# File: gui/dialogs/manage.py
# Desc: Manage Session Window
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from data import data
from gui.ui.managewindow_ui import Ui_MainWindow
from gui import gui_handle as handle
from gui.threads.create_thumbs import CreateThumbs
from gui.threads.watch_directory import WatchDirectory
from utils import helpers as h, watch
from gui.widgets.image_item import QImageItem
from gui.widgets.image_preview import ImagePreviewOverlay
from definitions import ROOT_DIR
import os
from functools import partial
from shutil import rmtree


class ManageWindow(QtWidgets.QStackedWidget):
    def __init__(self, parent, inst):
        super(ManageWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Vars
        self.session = inst
        self.parent = parent
        self.lists = [self.ui.photo_list]
        self.info_elms = [self.ui.img_name, self.ui.img_filename, self.ui.img_moddate]
        self.windows = [self.ui.photo_select, self.ui.proof_select, self.ui.final_select]
        self.open_msg = "Currently Open"
        self.watch = watch.watch
        ManageWindow.active_images = []
        self.current_window = "PHOTO"

        # Connections
        self.ui.home_button.clicked.connect(self.close)
        self.ui.photo_list.itemClicked.connect(self.update_info)
        self.ui.add_proof.clicked.connect(self.preview)
        self.ui.remove_proof.clicked.connect(self.remove_image)
        self.ui.img_name.returnPressed.connect(self.update_name)
        self.ui.create_button.clicked.connect(self.edit_photo)
        for el in self.windows:
            el.clicked.connect(partial(self.switch, el))

        # Thread
        self.threadpool = QtCore.QThreadPool()

        # Setup
        self.ui.session_name.setText(self.session.name)
        self.ui.progress.setValue(0)
        self.ui.progress.hide()
        self.create_thumbs()
        self.overlay = ImagePreviewOverlay
        self.update_images()
        self.watch_session(self.session.path)
        self.ui.create_button.setEnabled(False)
        handle.session_modify(self.session)

    # Functions
    def active_image(self):
        try:
            active = self.ui.photo_list.currentItem().data(QtCore.Qt.UserRole)
            self.ui.create_button.setEnabled(True)
            return active
        except AttributeError:
            self.clear()

    def create_thumbs(self):
        a = []

        def update(n):
            self.ui.progress.show()
            a.append(n)
            progress = int((len(a)/int(self.session.file_count))*100)
            self.ui.progress.setValue(progress)

        def finished():
            self.ui.progress.hide()

        def thumb(thumbs):
            for file, name in thumbs.items():
                img_cls = type(self.session.images[0])
                img = data.get_row(img_cls, file)
                thumb_path = f"{self.session.path}/thumbs/{name}"
                data.update_row(img, "thumb", thumb_path)
                print(img.thumb)

        worker = CreateThumbs(self.session.generate_thumbs, self.session)
        worker.signals.progress.connect(update)
        worker.signals.finished.connect(finished)
        worker.signals.thumbs.connect(thumb)
        self.threadpool.start(worker)

    def watch_session(self, path):
        def detect(file):
            print("DETECT ----")
            print(ManageWindow.active_images)
            for img in ManageWindow.active_images:
                print(img.name)
                match = img.check(file)
                if match is not False:
                    print(f"{img.name} MATCHED {file}")
                    match.set_jpg(file)
                else:
                    print('NO MATCH') #TODO: BACKUP METHODS
            self.update_images()

        worker = WatchDirectory(self.watch, path)
        worker.signals.created.connect(detect)
        self.threadpool.start(worker)

    def purge_thumbs(self): # TODO: MOVE THIS TO WHEN AN IMAGE IS POST-EDITED
        try:
            path = f"{self.session.path}/thumbs"
            rmtree(path)
            self.update_images()
        except FileNotFoundError:
            pass

    def preview(self):
        blur = QtWidgets.QGraphicsBlurEffect(self)
        blur.setBlurRadius(6)
        self.ui.contents.setGraphicsEffect(blur)
        self.addWidget(self.overlay(self, self.session))

    def close_preview(self, widget):
        self.ui.contents.setGraphicsEffect(None)
        self.removeWidget(widget)
        self.update_images()

    def update_images(self):
        print(self.current_window)
        self.ui.photo_list.clear()
        images = handle.get_images(self.session, self.current_window)
        open_images = handle.get_images(self.session, "OPEN")
        images.extend(open_images)
        self.ui.photo_list.setIconSize(QtCore.QSize(200, 200))
        for img in images:
            if img.position == "OPEN":
                widget = QImageItem(img, True)
            else:
                widget = QImageItem(img)
            print(widget.size())
            item = QtWidgets.QListWidgetItem(self.ui.photo_list)
            item.setData(QtCore.Qt.UserRole, img)
            item.setSizeHint(widget.size())
            self.ui.photo_list.addItem(item)
            self.ui.photo_list.setItemWidget(item, widget)

    def update_info(self):
        img = self.active_image()
        self.ui.img_name.setText(img.display)
        self.ui.img_filename.setText(img.name)
        if img.position != "PHOTO":
            img_name = os.path.basename(img.jpg)
            self.ui.img_filename.setText(img_name)
        if img.position == "OPEN":
            self.ui.img_filename.setText(img.name)
            self.ui.img_moddate.setText(self.open_msg)
            self.ui.create_button.setText("Finish")
        else:
            date = h.translate_date(img.modify)
            self.ui.img_moddate.setText(date)
            self.ui.create_button.setText("Edit")

    def update_name(self):
        img = self.active_image()
        name = self.ui.img_name.text()
        data.update_row(img, "display", name)

    def remove_image(self):
        img = self.active_image()
        handle.update_img(img, "RAW")
        self.ui.photo_list.clear()
        self.update_images()

    def edit_photo(self):
        img = self.active_image()
        if img.position == "PHOTO":
            item = self.ui.photo_list.currentItem()
            overlay = QImageItem(img, True)
            self.ui.photo_list.setItemWidget(item, overlay)
            img.set_active(True)
            ManageWindow.active_images = handle.get_actives(img)
            handle.update_img(img, "OPEN")
            handle.open_img(self.session, img)
            self.update_info()
        else:
            try:
                img.finalize(self.session)
            except FileNotFoundError as e:
                err_info = QtWidgets.QMessageBox()
                err_info.setWindowTitle('Session Manager')
                err_info.setText('Cannot Finalize image yet.')
                err_info.setInformativeText('You have not saved your image as a JPG yet. Please finish in Photoshop before finalizing.')
                err_info.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Retry)
                err_info_retry = err_info.button(QtWidgets.QMessageBox.Retry)
                err_info_retry.setText('Reopen')
                err_info.setDefaultButton(QtWidgets.QMessageBox.Ok)
                err_info.setDetailedText(str(e))
                err_info.setIcon(QtWidgets.QMessageBox.Warning)
                err_info.exec_()
                if err_info.clickedButton() == err_info_retry:
                    handle.open_img(self.session, img)
            self.update_images()
        self.clear()

    def switch(self, btn):
        self.clear()
        for el in self.windows:
            if el.isChecked():
                el.setChecked(False)
        btn.setChecked(True)
        if btn == self.ui.photo_select:
            self.ui.title.setText('PHOTOS')
            self.current_window = "PHOTO"
            self.update_images()
        if btn == self.ui.proof_select:
            self.ui.title.setText('PROOFS')
            self.current_window = "PROOF"
            self.update_images()
        if btn == self.ui.final_select:
            self.ui.title.setText('FINALS')
            self.current_window = "FINAL"
            self.update_images()

    def clear(self):
        for elm in self.info_elms:
            elm.clear()
        self.ui.create_button.setEnabled(False)

    def close(self):
        os.chdir(ROOT_DIR)
        self.parent.removeWidget(self)
        self.parent.setCurrentIndex(0)
        self.parent.close_window()


