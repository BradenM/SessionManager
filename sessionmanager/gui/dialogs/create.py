# Program: Session Manager
# File: gui/dialog/create.py
# Desc: Create Session Window
# Author: Braden Mars


from PyQt5 import QtCore, QtGui, QtWidgets
from gui import gui_handle as handle
from manage import handle as session
from gui.threads.create_session import CreateSession
from gui.ui.createwindow_ui import Ui_MainWindow
from definitions import ROOT_DIR
import os


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

        def update(n):
            self.ui.create_prog.show()
            self.ui.create_prog.setValue((n/len(images))*100)

        self.ui.error_info.hide()
        name = self.ui.create_name.text()
        path = self.ui.path_text.text()
        desc = self.ui.create_desc.toPlainText()
        raw = self.ui.keep_raw.checkState()

        if len(name) and len(desc) > 1:
            if handle.check_name_exist(name):
                self.ui.error_info.show()
                self.ui.error_info.setText("A session with the name '%s' already exist!" % name)
            else:
                self.ui.create_button.setDisabled(True)
                worker = CreateSession(session.create, name, path, desc, raw)
                worker.signals.progress.connect(update)
                worker.signals.finished.connect(finished)
                self.threadpool.start(worker)

        else:
            self.ui.error_info.show()
            self.ui.error_info.setText("Name and Description field must contain more than 1 character.")


