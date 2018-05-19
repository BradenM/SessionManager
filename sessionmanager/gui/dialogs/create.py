# Program: Session Manager
# File: gui/dialog/create.py
# Desc: Create Session Window
# Author: Braden Mars


from PyQt5 import QtCore, QtGui, QtWidgets
from gui import gui_handle as handle
from manage.session import Session
from gui.threads.create_session import CreateSession
from gui.ui.createwindow_ui import Ui_MainWindow
from definitions import ROOT_DIR
from data import data
import os


class CreateWindow(QtWidgets.QStackedWidget):
    def __init__(self, parent, path=None):
        super(CreateWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Vars
        self.session = Session
        self.parent = parent
        self.usb = path

        # Connections
        self.ui.open_path.clicked.connect(self.update_list)
        self.ui.create_button.clicked.connect(self.create)
        self.ui.create_button.setDisabled(True)
        self.ui.home_button.clicked.connect(self.close)

        # Setup Elements
        self.ui.error_info.hide()
        self.ui.create_prog.hide()
        self.clear()
        if self.usb is not None:
            self.ui.path_text.setText(self.usb)
            print(self.usb)

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
        def done():
            self.ui.create_prog.setValue(100)
            self.s.save()
            done_notif = QtWidgets.QSystemTrayIcon(QtGui.QIcon('icons/camera.png'))
            done_notif.show()
            done_notif.showMessage('Session Manager', f"Session '{name}' created successfully!")
            QtCore.QTimer().singleShot(2500, self.close)

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
            if data.row_exists(Session, name):
                self.ui.error_info.show()
                self.ui.error_info.setText("A session with the name '%s' already exist!" % name)
            else:
                self.ui.create_prog.setFormat("Processing...")
                self.ui.create_prog.show()
                self.ui.create_button.setDisabled(True)
                self.s = self.session(name)
                worker = CreateSession(self.s.setup, self.s.create, r_path, desc, raw)
                worker.signals.progress.connect(update)
                worker.signals.finished.connect(done)
                self.threadpool.start(worker)

        else:
            self.ui.error_info.show()
            self.ui.error_info.setText("Name and Description field must contain more than 1 character.")

    def clear(self):
        objects = [self.ui.create_name, self.ui.create_desc, self.ui.path_text, self.ui.image_list]
        for x in objects:
            x.clear()
        self.ui.create_prog.hide()

    def close(self):
        self.clear()
        os.chdir(ROOT_DIR)
        self.parent.removeWidget(self)
        self.parent.setCurrentIndex(0)
        self.parent.close_window()
