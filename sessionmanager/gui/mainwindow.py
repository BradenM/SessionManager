# Program: SessionManager
# File: gui/mainwindow.py
# Desc: SM Gui main window
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.mainwindow_ui import Ui_MainWindow
from manage.session import Session
from manage.usb import USB
from gui import gui_handle as handle
from gui.dialogs import create
from gui.dialogs import manage
from gui.dialogs.popup import Popup
from gui.animate import Animate
from gui.widgets.sessionitem import QSessionItem
from gui.widgets.event_filter import EventFilter
from gui.dialogs.settings_mod import SettingsModule
import qtawesome as fa
from data import data


class MainWindow(QtWidgets.QStackedWidget):
    def __init__(self, usb=None):
        super(MainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.MacWindowToolBarButtonHint | QtCore.Qt.CustomizeWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Vars
        self.session = Session
        self.animate = Animate(self)
        self.filter = EventFilter(self)
        self.setting_window = SettingsModule(self)
        self.setting_window.setVisible(False)
        self.delete_icon = fa.icon('fa.ban', color='red')
        self.create_window = create.CreateWindow
        self.manage_window = manage.ManageWindow
        self.info_elements = [self.ui.session_name, self.ui.create_date, self.ui.desc_box, self.ui.image_count, self.ui.has_raw, self.ui.modify_date]
        self.usb = usb
        self.threadpool = QtCore.QThreadPool()
        self.update_list()

        # Connections
        self.ui.sessionList.clicked.connect(self.update_info)
        #self.ui.centralwidget.mouseReleaseEvent=self.reset_info
        #self.ui.sesDelete.clicked.connect(self.delete_session)
        self.ui.session_filter.textChanged.connect(self.search_list)
        self.ui.create_tab.clicked.connect(self.create_session)
        self.ui.open_button.clicked.connect(self.open_session)
        self.ui.recent_button.clicked.connect(self.open_recent)
        self.ui.open_settings.clicked.connect(self.open_settings)
        # TODO: add completer to session_filter
        # Event Filters
        self.ui.create_tab.installEventFilter(self.filter)
        self.ui.create_tab.setProperty("action", "color_fade")
        self.ui.recent_button.installEventFilter(self.filter)
        self.ui.recent_button.setProperty("action", "color_fade")
        self.ui.open_settings.installEventFilter(self.filter)
        self.ui.open_settings.setProperty("action", "color_fade")
        self.ui.close_button.installEventFilter(self.filter)
        self.ui.close_button.setProperty("action", "color_mirror")
        self.ui.sessionList.installEventFilter(self.filter)
        self.ui.sessionList.setProperty("action", "context")
        #self.ui.session_filter.installEventFilter(self.ui.search_ico)
        #self.ui.search_ico.setProperty("animate", "color_fade")

        # Setup
        if self.usb is not None:
            self.create_session(path=self.usb)
        self.watch_usb()

    # Functions
    def active_session(self):
        try:
            item = self.ui.sessionList.currentItem().data(QtCore.Qt.UserRole)
            self.ui.open_button.setEnabled(True)
        except AttributeError:
            return False
        return item

    def update_list(self):
        self.ui.session_hint.hide()
        self.ui.sessionList.clear()
        sessions = data.iterate_table(self.session)
        for s in sessions:
            session_item = QSessionItem()
            session_item.set_name(s.name)
            session_item.set_icon("icons/camera.png")
            self.ui.sessionList.setGridSize(QtCore.QSize(200, 200))
            print(session_item.size())
            item = QtWidgets.QListWidgetItem(self.ui.sessionList)
            item.setData(QtCore.Qt.UserRole, s)
            item.setSizeHint(session_item.size())
            self.ui.sessionList.addItem(item)
            self.ui.sessionList.setItemWidget(item, session_item)
            print(item)
        count = len(sessions)
        self.ui.sessionlist_count.setText("(%s)" % count)
        self.reset_info()
        self.search_list()
        self.update_info()

    def update_info(self):
        item = self.active_session()
        if item is not False:
            s = handle.session_info(item)
            for i, elm in enumerate(self.info_elements):
                elm.setText(s[i])

    def reset_info(self):
        if self.ui.sessionList.count() >= 1:
            self.ui.sessionList.setCurrentItem(self.ui.sessionList.item(0))
            self.active_session()
        else:
            for el in self.info_elements:
                el.clear()
            self.ui.open_button.setDisabled(True)
            self.ui.session_hint.show()
        
    def delete_session(self):
        session = self.active_session()
        pop = Popup()
        delete = "Delete '%s'?" % session.name
        pop.setWindowTitle(delete)
        pop.ui.info.setText("WARNING:")
        pop.ui.desc.setText("Are you sure you want to delete '%s' ?" % session.name)
        check = pop.exec_()
        if check is 1:
            self.session.delete(session)
        self.ui.session_filter.clear()
        self.update_list()

    def search_list(self):
        filter = str(self.ui.session_filter.text()).lower()
        row_count = self.ui.sessionList.count()
        for row in range(row_count):
            item = self.ui.sessionList.item(row).data(QtCore.Qt.UserRole).name.lower()
            if filter in str(item):
                self.ui.sessionList.setRowHidden(row, False)
            else:
                self.ui.sessionList.setRowHidden(row, True)

    def watch_usb(self):
        def test(path):
            scan_result = USB().scan(path)
            if scan_result is not False:
                print("CAMERA MEMORY CARD DETECTED")
                self.create_session(path=scan_result)
        worker = USB()
        worker.signals.usb_detected.connect(test)
        self.threadpool.start(worker)

    def create_session(self, path=None):
        if path is not None:
            self.insertWidget(1, self.create_window(self, path=path))
        else:
            self.insertWidget(1, self.create_window(self))
        self.setCurrentIndex(1)

    def open_session(self):
        session = self.active_session()
        self.insertWidget(1, self.manage_window(self, session))
        self.setCurrentIndex(1)
        print('HERE')
        print(self.currentIndex())

    def open_recent(self):
        try:
            recent = handle.recent_session(self.session)
            self.insertWidget(1, self.manage_window(self, recent))
            self.setCurrentIndex(1)
        except ValueError:
            pass

    def open_settings(self):
        self.setting_window.setVisible(True)
        self.setting_window.raise_()

    def close_window(self):
        self.update_list()
