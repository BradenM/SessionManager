# Program: Session Manager
# File: threads/watch_directory.py
# Desc: Thread for watching directories
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from utils import watch


class WatchDirectory(QtCore.QThread):

    def __init__(self, path):
        QtCore.QThread.__init__(self)
        self.path = path

    def __del__(self):
        self.wait()

    def run(self):
        watch.watch(self.path)
