# Program: Session Manager
# File: gui/threads/setup_session.py
# Desc: Create session GUI thread
# Author: Braden Mars

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class WorkerSignals(QObject):
    finished = pyqtSignal()


class SetupSession(QRunnable):
    def __init__(self, fn, path, desc, raw, *args, **kwargs):
        super(SetupSession, self).__init__()
        self.signals = WorkerSignals()
        self.path = path
        self.desc = desc
        self.raw = raw
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        try:
            self.fn(self.path, self.desc, self.raw, *self.args, **self.kwargs)
        finally:
            self.signals.finished.emit()

