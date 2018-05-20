# Program: Session Manager
# File: gui/dialogs/usb_pop.py
# Desc: USB Detect Popup Window
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.usbwindow_ui import Ui_USBWindow
from gui.mainwindow import MainWindow
import time


class USBSignals(QtCore.QObject):
    found = QtCore.pyqtSignal()


class USBStalk(QtCore.QRunnable):
    def __init__(self, usb):
        super(USBStalk, self).__init__()
        # Vars
        self.signals = USBSignals()
        self.usb = usb
        self.found = self.signals.found

    @QtCore.pyqtSlot()
    def run(self):
        while self.usb.found is False:
            time.sleep(3)
        print('found emitted')
        self.found.emit()


class USBWindow(QtWidgets.QWidget):
    def __init__(self, usb):
        super(USBWindow, self).__init__()
        self.ui = Ui_USBWindow()
        self.ui.setupUi(self)
        # Vars
        self.usb = usb
        self.threadpool = QtCore.QThreadPool()

        # Connections
        self.ui.create.clicked.connect(self.create)
        self.ui.close.clicked.connect(self.stalk)

        # Setup

    # Functions

    def create(self):
        window = MainWindow(usb=self.usb.path)
        window.show()
        self.close()

    def reveal(self):
        print('revealed')
        self.show()

    def stalk(self):
        self.hide()
        self.usb.found = False

        worker = USBStalk(self.usb)
        worker.signals.found.connect(self.reveal)
        self.threadpool.start(worker)

