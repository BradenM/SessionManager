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
from gui.widgets.proof_overlay import ProofOverlay
from gui.widgets.edit_overlay import EditOverlay
from gui.widgets.popup import PopupMsg
from definitions import ROOT_DIR
import os
from functools import partial


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
        self.windows = [self.ui.photo_select, self.ui.final_select]
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
        self.ui.export.clicked.connect(self.export_proofs)
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
        self.proofs = ProofOverlay
        self.edit_overlay = EditOverlay
        self.update_images()
        self.watch_session()
        self.ui.create_button.setEnabled(False)
        self.ui.crop_combo.setHidden(True)
        self.ui.crop_title.setHidden(True)
        self.ui.export.setHidden(True)
        self.ui.export.setEnabled(False)
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

    def watch_session(self):
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

        worker = WatchDirectory(self.watch, self.session.path)
        worker.signals.created.connect(detect)
        self.threadpool.start(worker)

    def preview(self):
        blur = QtWidgets.QGraphicsBlurEffect(self)
        blur.setBlurRadius(6)
        self.ui.contents.setGraphicsEffect(blur)
        self.addWidget(self.overlay(self, self.session))

    def close_preview(self, widget):
        self.ui.contents.setGraphicsEffect(None)
        self.removeWidget(widget)
        self.update_images()

    def view_proofs(self, img):
        blur = QtWidgets.QGraphicsBlurEffect(self)
        blur.setBlurRadius(6)
        self.ui.contents.setGraphicsEffect(blur)
        self.addWidget(self.proofs(self, img))

    def edit_proofs(self, parent_widget, img):
        self.close_preview(parent_widget)
        self.parent.resize(1200, 700)
        self.resize(1200, 700)
        print(self.parent.size())
        # blur = QtWidgets.QGraphicsBlurEffect(self)
        # blur.setBlurRadius(6)
        # self.ui.contents.setGraphicsEffect(blur)
        self.addWidget(self.edit_overlay(self, img))

    def update_images(self, imgs=None):
        print(self.current_window)
        self.ui.photo_list.clear()
        if imgs is not None:
            images = imgs
        else:
            images = handle.get_images(self.session, self.current_window)
            if len(images) > 1:
                self.ui.export.setEnabled(True)
                print("EXPORT ENABLED")
        if self.current_window == "PHOTO":
            open_images = handle.get_images(self.session, "OPEN")
            images.extend(open_images)
        self.ui.photo_list.setIconSize(QtCore.QSize(200, 200))
        for img in images:
            try:
                if img.position == "OPEN":
                    widget = QImageItem(img, True)
                else:
                    widget = QImageItem(img)
            except AttributeError:
                widget = QImageItem(img)
                print('No Position in Proof')
            print(widget.size())
            item = QtWidgets.QListWidgetItem(self.ui.photo_list)
            item.setData(QtCore.Qt.UserRole, img)
            item.setSizeHint(widget.size())
            self.ui.photo_list.setGridSize(widget.size())
            self.ui.photo_list.addItem(item)
            self.ui.photo_list.setItemWidget(item, widget)

    def update_info(self):
        img = self.active_image()
        date = h.translate_date(img.modify)
        self.ui.img_name.setText(img.display)
        self.ui.img_filename.setText(img.name)
        jpg_name = os.path.basename(img.jpg)
        if img.position != "PHOTO":
            self.ui.img_filename.setText(jpg_name)
        if img.position == "OPEN":
            self.ui.img_filename.setText(img.name)
            self.ui.img_moddate.setText(self.open_msg)
            self.ui.create_button.setText("Finish")
        elif img.position == "FINAL":
            self.ui.img_filename.setText(jpg_name)
            self.ui.img_moddate.setText(date)
            self.ui.create_button.setText("Proofs")
        else:
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
        elif img.position == "FINAL" and self.current_window != "PROOF":
            self.view_proofs(img)
        elif img.position == "FINAL" and self.current_window == "PROOF":
            print("LOAD PROOFS")
            imgs = handle.get_proofs(img, 1)
            self.update_images(imgs)
        else:
            try:
                img.finalize(self.session)
            except FileNotFoundError as e:
                pop = PopupMsg(self, PopupMsg.F_ERROR, e)
                if pop:
                    handle.open_img(self.session, img)
            self.update_images()
        self.clear()

    def export_proofs(self):
        dialog = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select a Directory"))
        for img in self.session.images:
            ex_path = img.export_proof(dialog)
        h.open_dir(ex_path)

    def switch(self, btn):
        self.clear()
        for el in self.windows:
            if el.isChecked():
                el.setChecked(False)
        btn.setChecked(True)
        if btn == self.ui.photo_select:
            self.ui.title.setText('PHOTOS')
            self.current_window = "PHOTO"
            self.ui.export.setHidden(True)
            self.update_images()
        if btn == self.ui.final_select:
            self.ui.title.setText('FINALS')
            self.current_window = "FINAL"
            self.ui.crop_combo.setHidden(True)
            self.ui.crop_title.setHidden(True)
            self.ui.export.setHidden(False)
            self.update_images()

    def clear(self):
        for elm in self.info_elms:
            elm.clear()
        self.ui.create_button.setEnabled(False)
        self.ui.crop_combo.setHidden(True)
        self.ui.crop_title.setHidden(True)

    def close(self):
        os.chdir(ROOT_DIR)
        self.parent.removeWidget(self)
        self.parent.setCurrentIndex(0)
        self.parent.close_window()


