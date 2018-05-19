# Program: Session Manager
# File: gui/dialogs/usb_pop.py
# Desc: USB Detect Popup Window
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.usbwindow_ui import Ui_USBWindow
from gui.mainwindow import MainWindow
import sys


class USBWindow(QtWidgets.QWidget):
    def __init__(self, path):
        super(USBWindow, self).__init__()
        self.ui = Ui_USBWindow()
        self.ui.setupUi(self)
        # Vars
        self.path = path

        # Connections
        self.ui.create.clicked.connect(self.create)
        self.ui.close.clicked.connect(lambda x: self.close())

        # Setup

    # Functions

    def create(self):
        window = MainWindow(usb=self.path)
        window.show()
        self.close()