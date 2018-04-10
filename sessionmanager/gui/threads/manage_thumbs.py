# Program: Session Manager
# File: gui/threads/manage_thumbs.py
# Desc: Thread for managing Thumbnails in ManageSession Window
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from gui import gui_handle as handle


class ManageThumbs(QtCore.QThread):
    working = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()
    raw = QtCore.pyqtSignal(object)
    proof = QtCore.pyqtSignal(object)
    final = QtCore.pyqtSignal(object)

    def __init__(self, path):
        QtCore.QThread.__init__(self)
        self.path = path

    def __del__(self):
        self.wait()

    def run(self):
        self.working.emit()
        raw, proof, final= handle.get_thumbs(self.path)
        for x in raw:
            self.raw.emit(x)
        for x in proof:
            self.proof.emit(x)
        for x in final:
            self.final.emit(x)
        self.finished.emit()

