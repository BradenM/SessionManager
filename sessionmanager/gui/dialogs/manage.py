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
from utils import process
from gui.widgets.imageitem import QImageItem
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
        self.ui.add_proof.clicked.connect(self.preview)

        # Thread
        self.threadpool = QtCore.QThreadPool()

        # Vars
        self.session = inst
        self.parent = parent

        # Setup
        self.ui.session_name.setText(self.session.name)
        self.ui.progress.setValue(0)
        self.ui.progress.hide()
        self.create_thumbs()
        self.overlay = ImagePreviewOverlay

    # Functions
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

    def close_overlay(self, widget):
        self.ui.contents.setGraphicsEffect(None)
        self.removeWidget(widget)

    def update_images(self):
        pass

    def close(self):
        #self.clear()
        os.chdir(ROOT_DIR)
        window = self.currentWidget()
        self.parent.setCurrentIndex(0)
        self.parent.close_window(window)
