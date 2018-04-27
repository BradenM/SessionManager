# Program: Session Manager
# File: gui/threads/create_session.py
# Desc: Create session GUI thread
# Author: Braden Mars

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class WorkerSignals(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(list)


class CreateSession(QRunnable):
    def __init__(self, setup_fn, create_fn, path, desc, raw, *args, **kwargs):
        super(CreateSession, self).__init__()
        self.signals = WorkerSignals()
        self.path = path
        self.desc = desc
        self.raw = raw
        self.setup = setup_fn
        self.create = create_fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        def update(ch):
            self.signals.progress.emit(ch)
        try:
            self.setup(self.path, self.desc, self.raw, *self.args)
        finally:
            self.create(update)
            self.signals.finished.emit()
