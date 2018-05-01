# Program: Session Manager
# File: gui/app.py
# Desc: GUI Start file
# Author: Braden Mars

import sys
from gui.mainwindow import MainWindow
from PyQt5 import QtWidgets, QtCore


def main():
    QtWidgets.QApplication.setStyle('Fusion')
    window = MainWindow()
    window.show()
    return QtWidgets.qApp.exec_()


def start():
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(main())

