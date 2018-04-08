# Program: Session Manager
# File: gui/threads/create_session.py
# Desc: Create session GUI thread
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from manage import handle
import os
from manage import manage as m


class CreateSession(QtCore.QThread):
    working = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()

    def __init__(self, name, path, desc, raw):
        QtCore.QThread.__init__(self)
        self.name = name
        self.path = path
        self.desc = desc
        self.raw = raw

    def __del__(self):
        self.wait()

    def run(self):
        self.working.emit()
        handle.create(self.name, self.path, self.desc, self.raw)
        return self.finished.emit()


