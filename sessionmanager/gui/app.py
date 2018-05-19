# Program: Session Manager
# File: gui/app.py
# Desc: GUI Start file
# Author: Braden Mars

import sys
from gui.mainwindow import MainWindow
from gui.dialogs.usb_pop import USBWindow
from PyQt5 import QtWidgets, QtCore


def main():
    QtWidgets.QApplication.setStyle('Fusion')
    window = MainWindow()
    window.show()
    return QtWidgets.qApp.exec_()


def usb(path):
    QtWidgets.QApplication.setStyle('Fusion')
    ui = USBWindow(path)
    ui.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ui.show()
    return QtWidgets.qApp.exec_()


def start_usb(path):
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(usb(path))


def start():
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(main())


