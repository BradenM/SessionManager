# Program: Session Manager
# File: gui/threads/create_session.py
# Desc: Create session GUI thread
# Author: Braden Mars

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class WorkerSignals(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)


class CreateSession(QRunnable):
    def __init__(self, fn, name, path, desc, raw, *args, **kwargs):
        super(CreateSession, self).__init__()
        self.signals = WorkerSignals()
        kwargs['prog_callback'] = self.signals.progress
        self.name = name
        self.path = path
        self.desc = desc
        self.raw = raw
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        try:
            self.fn(self.name, self.path, self.desc, self.raw, *self.args, **self.kwargs)
        finally:
            self.signals.finished.emit()
