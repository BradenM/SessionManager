# Program: Session Manager
# File: gui/dialog/create.py
# Desc: Create Session Window
# Author: Braden Mars


from PyQt5 import QtCore, QtGui, QtWidgets
from gui import gui_handle as handle
from manage.session import Session
from gui.threads.setup_session import SetupSession
from gui.ui.createwindow_ui import Ui_MainWindow
from definitions import ROOT_DIR
import os
import time


class CreateWindow(QtWidgets.QStackedWidget):
    def __init__(self, parent):
        super(CreateWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connections
        self.ui.open_path.clicked.connect(self.update_list)
        self.ui.create_button.clicked.connect(self.create)
        self.ui.create_button.setDisabled(True)
        self.ui.home_button.clicked.connect(parent.close_window)

        # Setup Elements
        self.ui.error_info.hide()
        self.ui.create_prog.hide()

        # Thread
        self.threadpool = QtCore.QThreadPool()

        # Vars
        self.session = Session

    # Functions
    def update_list(self):
        global dialog
        dialog = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select a Directory"))
        self.ui.path_text.setText(dialog)
        self.ui.image_list.clear()
        self.update_image()

    def update_image(self):
        self.ui.error_info.clear()
        if os.path.isdir(dialog):
            global images
            images, items = handle.update_images(dialog)
            if len(images) < 1:
                self.ui.error_info.show()
                self.ui.error_info.setText("This directory holds no RAW images.")
            else:
                self.ui.create_button.setDisabled(False)
                for x in items:
                    self.ui.image_list.addItem(x)
        else:
            self.ui.error_info.show()
            self.ui.error_info.setText("Invalid Path, please select another.")

    def create(self):
        def finished():
            self.ui.create_prog.setValue(100)
            QtCore.QTimer().singleShot(2500, lambda: self.ui.home_button.click())

        a = []

        def update(n):
            self.ui.create_prog.setMaximum(100)
            self.ui.create_prog.setFormat("%p%")
            a.extend(n)
            progress = int((len(a) / int(len(images))) * 100)
            self.ui.create_prog.setValue(progress)

        self.ui.error_info.hide()
        name = self.ui.create_name.text()
        r_path = self.ui.path_text.text()
        desc = self.ui.create_desc.toPlainText()
        raw = self.ui.keep_raw.checkState()

        if len(name) and len(desc) > 1:
            if self.session(name).exist():
                self.ui.error_info.show()
                self.ui.error_info.setText("A session with the name '%s' already exist!" % name)
            else:
                self.ui.create_prog.show()
                self.ui.create_button.setDisabled(True)
                # worker = SetupSession(s.setup, r_path, desc, raw)
                # self.threadpool.start(worker)
                s = self.session(name)
                s.setup(r_path, desc, raw)
                s.create(update)
                finished()

        else:
            self.ui.error_info.show()
            self.ui.error_info.setText("Name and Description field must contain more than 1 character.")


