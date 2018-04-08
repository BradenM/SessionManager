# Program: Session Manager
# File: gui/dialog/create.py
# Desc: Create Session Window
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from definitions import ROOT_DIR
from gui.ui.createwindow_ui import Ui_createWindow
from gui import gui_handle as handle
from gui.threads.create_session import CreateSession
import os


class CreateWindow(QtWidgets.QDialog):
    def __init__(self):
        super(CreateWindow, self).__init__()
        self.ui = Ui_createWindow()
        self.ui.setupUi(self)

        # Connections
        self.ui.openPath.clicked.connect(self.update_list)
        self.ui.cancelButton.clicked.connect(self.reject)
        self.ui.createButton.clicked.connect(self.create)
        self.ui.createButton.setDisabled(True)

        # Load Connections
        global gif
        gif = QtGui.QMovie("%s/icons/loading.gif" % ROOT_DIR)
        self.ui.loadingGif.setMovie(gif)
        self.ui.loadingGif.hide()
        self.ui.loadingText.hide()
        self.ui.errorInfo.hide()

    # Functions
    def update_list(self):
        global dialog
        dialog = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select a Directory"))
        self.ui.pathText.setText(dialog)
        self.ui.imageList.clear()
        self.update_image()

    def update_image(self):
        self.ui.errorInfo.clear()
        if os.path.isdir(dialog):
            images, items = handle.update_images(dialog)
            if len(images) < 1:
                self.ui.errorInfo.show()
                self.ui.errorInfo.setText("This directory holds no RAW images.")
            else:
                self.ui.createButton.setDisabled(False)
                for x in items:
                    self.ui.imageList.addItem(x)
        else:
            self.ui.errorInfo.show()
            self.ui.errorInfo.setText("Invalid Path, please select another.")

    def create(self):
        def finished():
            gif.stop()
            self.ui.loadingGif.clear()
            self.ui.loadingGif.setText("")
            self.ui.loadingText.setText("Finished!")
            QtCore.QTimer().singleShot(2500, lambda: self.close())

        def working():
            gif.start()
            self.ui.loadingGif.show()
            self.ui.loadingText.show()
            self.ui.createButton.setDisabled(True)

        self.ui.errorInfo.hide()
        name = self.ui.createName.text()
        path = self.ui.pathText.text()
        desc = self.ui.createDesc.text()
        raw = self.ui.keepRaw.checkState()

        if len(name) and len(desc) > 1:
            if handle.check_name_exist(name):
                self.ui.errorInfo.show()
                self.ui.errorInfo.setText("A session with the name '%s' already exist!" % name)
            else:
                self.get_thread = CreateSession(name, path, desc, raw)
                self.get_thread.finished.connect(finished)
                self.get_thread.working.connect(working)
                self.get_thread.start()
        else:
            self.ui.errorInfo.show()
            self.ui.errorInfo.setText("Name and Description field must contain more than 1 character.")