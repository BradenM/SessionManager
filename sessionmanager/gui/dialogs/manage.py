# Program: Session Manager
# File: gui/dialogs/manage.py
# Desc: Manage Session Window
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.managewindow_ui import Ui_MainWindow
from gui import gui_handle as handle
from gui.threads.create_thumbs import CreateThumbs
from gui.threads.watch_directory import WatchDirectory
from utils import process
import time

class ManageWindow(QtWidgets.QWidget):
    def __init__(self, parent, name):
        super(ManageWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.name = name

        # Connections
        self.ui.home_button.clicked.connect(parent.close_window)
        self.ui.add_proof.clicked.connect(self.create_thumbs)

        # Thread
        self.threadpool = QtCore.QThreadPool()

        # Vars
        _, _, self.path, self.count, _, _ = handle.get_info(self.name)

        # Setup
        self.ui.session_name.setText(self.name)
        self.ui.progress.setValue(0)

    # Functions
    def create_thumbs(self):
        a = []
        def update(n):
            a.append(n)
            progress = int((len(a)/int(self.count))*100)
            self.ui.progress.setValue(progress)

        def finished():
            QtCore.QTimer().singleShot(2500, lambda: self.ui.progress.hide())

        worker = CreateThumbs(process.generate_thumbs, self.path)
        worker.signals.progress.connect(update)
        worker.signals.finished.connect(finished)
        self.threadpool.start(worker)
        #progress = QtCore.pyqtSignal(str)
        # kwargs = dict()
        # kwargs['prog_callback'] = progress
        #process.generate_thumbs(self.path, update)

