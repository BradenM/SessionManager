# Program: Session Manager
# File: threads/watch_directory.py
# Desc: Thread for watching directories
# Author: Braden Mars

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class WorkerSignals(QObject):
    created = pyqtSignal(str)


class WatchDirectory(QRunnable):
    def __init__(self, fn, path, quit=False, *args, **kwargs):
        super(WatchDirectory, self).__init__()
        # Vars
        self.signals = WorkerSignals()
        kwargs['callback'] = self.signals.created
        self.fn = fn
        self.path = path
        self.quit = quit
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        try:
            self.fn(self.path, self.quit, *self.args, **self.kwargs)
        finally:
            print('complete')
