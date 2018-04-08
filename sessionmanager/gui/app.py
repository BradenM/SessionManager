# Program: Session Manager
# File: gui/app.py
# Desc: GUI Start file
# Author: Braden Mars

import sys
from gui.mainwindow import MainWindow
from PyQt5 import QtWidgets


def start():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.update_list()
    sys.exit(app.exec_())

