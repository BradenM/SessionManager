# Program: Session Manager
# File: gui/threads/create_thumbs.py
# Desc: Thread for managing Thumbnails in ManageSession Window
# Author: Braden Mars

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class WorkerSignals(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    thumbs = pyqtSignal(dict)


class CreateThumbs(QRunnable):
    def __init__(self, fn, inst, *args, **kwargs):
        super(CreateThumbs, self).__init__()
        # Vars
        self.signals = WorkerSignals()
        kwargs['callback'] = self.signals.progress
        kwargs['thumb_call'] = self.signals.thumbs
        self.fn = fn
        self.inst = inst
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        try:
            self.fn(self.inst, *self.args, **self.kwargs)
        finally:
            self.signals.finished.emit()
