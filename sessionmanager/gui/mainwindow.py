# Program: SessionManager
# File: gui/mainwindow.py
# Desc: SM Gui main window
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.mainwindow_ui import Ui_MainWindow
from gui import gui_handle as handle
from gui.dialogs.create import CreateWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connections
        self.ui.sessionList.clicked.connect(self.update_info)
        self.ui.centralwidget.mouseReleaseEvent=self.reset_info
        self.ui.sesDelete.clicked.connect(self.delete_session)
        self.ui.sesFilter.textChanged.connect(self.search_list)
        self.ui.createSesButton.clicked.connect(self.create_session)
        # TODO: add completer to sesFilter
        # Elements
        self.ui.sesDelete.hide()

    # Functions
    def update_list(self):
        self.ui.sessionList.clear()
        items = handle.iterate_sessions()
        for x in items:
            self.ui.sessionList.addItem(x)

    def update_info(self):
        item = self.ui.sessionList.currentItem().text()
        date, desc = handle.get_info(item)
        self.ui.sesName.setText(item)
        self.ui.date_text.setText(date)
        self.ui.desc_Box.setText(desc)
        self.ui.sesDelete.show()

    def reset_info(self, event):
        self.ui.sesName.clear()
        self.ui.date_text.clear()
        self.ui.desc_Box.clear()
        self.ui.sesDelete.hide()
        
    def delete_session(self):
        item = self.ui.sessionList.currentItem().text()
        handle.delete_session(item)
        self.ui.sesFilter.clear()
        self.update_list()
        self.reset_info(event=None)

    def search_list(self):
        filter = str(self.ui.sesFilter.text()).lower()
        row_count = self.ui.sessionList.count()
        for row in range(row_count):
            item = self.ui.sessionList.item(row).text().lower()
            if filter in str(item):
                self.ui.sessionList.setRowHidden(row, False)
            else:
                self.ui.sessionList.setRowHidden(row, True)

    def create_session(self):
        window = CreateWindow()
        window.exec_()
        self.update_list()