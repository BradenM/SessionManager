# Program: SessionManager
# File: gui/mainwindow.py
# Desc: SM Gui main window
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.mainwindow_ui import Ui_MainWindow
from gui import gui_handle as handle
from gui.dialogs.manage import ManageWindow
from gui.dialogs import create
import time
import sip

class MainWindow(QtWidgets.QStackedWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connections
        self.ui.sessionList.clicked.connect(self.update_info)
        #self.ui.centralwidget.mouseReleaseEvent=self.reset_info
        #self.ui.sesDelete.clicked.connect(self.delete_session)
        self.ui.session_filter.textChanged.connect(self.search_list)
        self.ui.create_tab.clicked.connect(self.create_session)
        self.ui.open_button.clicked.connect(self.open_session)
        self.create_window = create.CreateWindow(self)
        # TODO: add completer to session_filter
        # Elements
        #self.ui.sesDelete.hide()




    # Functions
    def update_list(self):
        self.ui.sessionList.clear()
        items = handle.iterate_sessions()
        for x in items:
            self.ui.sessionList.addItem(x)
        count = str(self.ui.sessionList.count())
        self.ui.sessionlist_count.setText("(%s)" % count)
        if self.ui.sessionList.count() >= 1:
            self.ui.sessionList.setCurrentItem(self.ui.sessionList.item(0))
            self.update_info()

    def update_info(self):
        item = self.ui.sessionList.currentItem().text()
        date, desc, _ , count, raw, modify = handle.get_info(item)
        #self.ui.sesName.setText(item)
        self.ui.create_date.setText(date)
        self.ui.desc_box.setText(desc)
        self.ui.image_count.setText(count)
        self.ui.has_raw.setText(raw)
        self.ui.modify_date.setText(modify)
        #self.ui.sesDelete.show()
        self.ui.open_button.setDisabled(False)

    def reset_info(self, event):
        #self.ui.sesName.clear()
        self.ui.create_date.clear()
        self.ui.desc_box.clear()
        #self.ui.sesDelete.hide()
        self.ui.open_button.setDisabled(True)
        
    def delete_session(self):
        item = self.ui.sessionList.currentItem().text()
        handle.delete_session(item)
        self.ui.session_filter.clear()
        self.update_list()
        self.reset_info(event=None)

    def search_list(self):
        filter = str(self.ui.session_filter.text()).lower()
        row_count = self.ui.sessionList.count()
        for row in range(row_count):
            item = self.ui.sessionList.item(row).text().lower()
            if filter in str(item):
                self.ui.sessionList.setRowHidden(row, False)
            else:
                self.ui.sessionList.setRowHidden(row, True)

    def create_session(self):
        self.create_window = create.CreateWindow(self)
        print(self.currentIndex())
        self.addWidget(self.create_window)
        self.setCurrentIndex(1)

    def open_session(self):
        name = self.ui.sessionList.currentItem().text()
        self.hide()
        window = ManageWindow(name)
        window.exec_()
        self.show()

    def close_window(self):
        window = self.currentWidget()
        self.removeWidget(window)
        sip.delete(self.create_window)
        self.create_window = None
        self.setCurrentIndex(0)
