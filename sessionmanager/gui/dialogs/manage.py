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
from utils import shop_bridge
from gui.widgets.image_item import QImageItem
from gui.widgets.image_preview import ImagePreviewOverlay
from definitions import ROOT_DIR
import os


class ManageWindow(QtWidgets.QStackedWidget):
    def __init__(self, parent, inst):
        super(ManageWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connections
        self.ui.home_button.clicked.connect(self.close)
        self.ui.photo_list.itemClicked.connect(self.update_info)
        self.ui.add_proof.clicked.connect(self.preview)
        self.ui.remove_proof.clicked.connect(self.remove_image)
        self.ui.img_name.returnPressed.connect(self.update_name)
        self.ui.create_button.clicked.connect(self.edit_photo)

        # Thread
        self.threadpool = QtCore.QThreadPool()

        # Vars
        self.session = inst
        self.parent = parent
        self.lists = [self.ui.photo_list]
        self.open_msg = "Currently Open"

        # Setup
        self.ui.session_name.setText(self.session.name)
        self.ui.progress.setValue(0)
        self.ui.progress.hide()
        self.create_thumbs()
        self.overlay = ImagePreviewOverlay
        self.update_images()

    # Functions
    def active_image(self):
        active = self.ui.photo_list.currentItem().data(QtCore.Qt.UserRole)
        return active

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

    def preview(self):
        blur = QtWidgets.QGraphicsBlurEffect(self)
        blur.setBlurRadius(6)
        self.ui.contents.setGraphicsEffect(blur)
        self.addWidget(self.overlay(self, self.session))

    def close_preview(self, widget):
        self.update()
        self.ui.contents.setGraphicsEffect(None)
        self.removeWidget(widget)
        self.update_images()

    def update_images(self):
        self.ui.photo_list.clear()
        images = handle.get_images(self.session, "PHOTO")
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
        if img.position == "OPEN":
            self.ui.img_moddate.setText(self.open_msg)
            self.ui.create_button.setText("Finish")
        else:
            self.ui.img_moddate.setText(str(img.modify))
            self.ui.create_button.setText("Edit")

    def update_name(self):
        img = self.active_image()
        name = self.ui.img_name.text()
        data.update_row(img, "display", name)

    def remove_image(self):
        img = self.active_image()
        handle.update_pos(img, "RAW")
        self.ui.photo_list.clear()
        self.update_images()

    def edit_photo(self):
        img = self.active_image()
        overlay = QImageItem(img, True)
        item = self.ui.photo_list.currentItem()
        self.ui.photo_list.setItemWidget(item, overlay)
        if img.position == "PHOTO":
            handle.update_pos(img, "OPEN")
            handle.update_modify(img)
            shop_bridge.ps_open(img.path)
        else:
            handle.update_pos(img, "FINAL")
        self.update_info()

    def close(self):
        os.chdir(ROOT_DIR)
        self.parent.removeWidget(self)
        self.parent.setCurrentIndex(0)
        self.parent.close_window()


