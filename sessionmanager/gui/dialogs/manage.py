# Program: Session Manager
# File: gui/dialogs/manage.py
# Desc: Manage Session Window
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from manage.session import Session
from gui.ui.managewindow_ui import Ui_MainWindow
from gui import gui_handle as handle
from gui.threads.create_thumbs import CreateThumbs
from gui.threads.watch_directory import WatchDirectory
from utils import process
from gui.widgets.imageitem import QImageItem


class ManageWindow(QtWidgets.QWidget):
    def __init__(self, parent, name):
        super(ManageWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connections
        self.ui.home_button.clicked.connect(parent.close_window)
        self.ui.add_proof.clicked.connect(self.create_thumbs)

        # Thread
        self.threadpool = QtCore.QThreadPool()

        # Vars
        self.name = name
        self.session = Session(name)
        self.info = self.session.info()

        # Setup
        self.ui.session_name.setText(self.name)
        self.ui.progress.setValue(0)
        self.ui.progress.hide()

    # Functions
    def create_thumbs(self):
        a = []
        def update(n):
            self.ui.progress.show()
            a.append(n)
            progress = int((len(a)/int(self.info['count']))*100)
            self.ui.progress.setValue(progress)

        def finished():
            self.ui.progress.hide()

        worker = CreateThumbs(self.session.generate_thumbs)
        worker.signals.progress.connect(update)
        worker.signals.finished.connect(finished)
        self.threadpool.start(worker)

    def update_thumbs(self):
        thumbs = process.iterate_thumbs(self.path)

