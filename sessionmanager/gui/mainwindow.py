# Program: SessionManager
# File: gui/mainwindow.py
# Desc: SM Gui main window
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.mainwindow_ui import Ui_MainWindow
from manage.session import Session
from gui import gui_handle as handle
from gui.dialogs import create
from gui.dialogs import manage
from gui.dialogs.popup import Popup
from gui.animate import Animate
from gui.widgets.sessionitem import QSessionItem
import qtawesome as fa

from data import data


class MainWindow(QtWidgets.QStackedWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.MacWindowToolBarButtonHint | QtCore.Qt.CustomizeWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connections
        self.ui.sessionList.clicked.connect(self.update_info)
        #self.ui.centralwidget.mouseReleaseEvent=self.reset_info
        #self.ui.sesDelete.clicked.connect(self.delete_session)
        self.ui.session_filter.textChanged.connect(self.search_list)
        self.ui.create_tab.clicked.connect(self.create_session)
        self.ui.open_button.clicked.connect(self.open_session)
        # TODO: add completer to session_filter
        # Event Filters
        self.ui.create_tab.installEventFilter(self)
        self.ui.create_tab.setProperty("action", "color_fade")
        self.ui.pushButton_4.installEventFilter(self)
        self.ui.pushButton_4.setProperty("action", "color_fade")
        self.ui.pushButton_2.installEventFilter(self)
        self.ui.pushButton_2.setProperty("action", "color_fade")
        self.ui.close_button.installEventFilter(self)
        self.ui.close_button.setProperty("action", "color_mirror")
        self.ui.sessionList.installEventFilter(self)
        self.ui.sessionList.setProperty("action", "context")
        #self.ui.session_filter.installEventFilter(self.ui.search_ico)
        #self.ui.search_ico.setProperty("animate", "color_fade")

        # Vars
        self.session = Session
        self.animate = Animate(self)
        self.delete_icon = fa.icon('fa.ban', color='red')
        self.create_window = create.CreateWindow(self)
        self.info_elements = [self.ui.session_name, self.ui.create_date, self.ui.desc_box, self.ui.image_count, self.ui.has_raw, self.ui.modify_date]
        self.update_list()


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
            item.setData(QtCore.Qt.UserRole, s.name)
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
            s = handle.session_info(self.session, item)
            for i, elm in enumerate(self.info_elements):
                elm.setText(s[i])

    def reset_info(self):
        if self.ui.sessionList.count() >= 1:
            self.ui.sessionList.setCurrentItem(self.ui.sessionList.item(0))
        else:
            for el in self.info_elements:
                el.clear()
            self.ui.open_button.setDisabled(True)
            self.ui.session_hint.show()
        
    def delete_session(self):
        name = self.active_session()
        session = data.get_row(self.session, name)
        pop = Popup()
        delete = "Delete '%s'?" % name
        pop.setWindowTitle(delete)
        pop.ui.info.setText("WARNING:")
        pop.ui.desc.setText("Are you sure you want to delete '%s' ?" % name)
        check = pop.exec_()
        if check is 1:
            self.session.delete(session)
        self.ui.session_filter.clear()
        self.update_list()

    def search_list(self):
        filter = str(self.ui.session_filter.text()).lower()
        row_count = self.ui.sessionList.count()
        for row in range(row_count):
            item = self.ui.sessionList.item(row).data(QtCore.Qt.UserRole).lower()
            if filter in str(item):
                self.ui.sessionList.setRowHidden(row, False)
            else:
                self.ui.sessionList.setRowHidden(row, True)

    def create_session(self):
        self.addWidget(self.create_window)
        self.setCurrentIndex(1)

    def open_session(self):
        item = self.ui.sessionList.currentItem().data(QtCore.Qt.UserRole)
        session = data.get_row(self.session, item)
        self.addWidget(manage.ManageWindow(self, session))
        self.setCurrentIndex(1)

    def close_window(self, window):
        self.removeWidget(window)
        self.update_list()

    def eventFilter(self, object, event):
        action = str(object.property("action"))
        if action == "color_fade":
            if event.type() == QtCore.QEvent.HoverEnter:
                self.animate.color_fade(object, "#736F6E", "#f2f2f2")
                return True
            if event.type() == QtCore.QEvent.HoverLeave:
                self.animate.color_fade(object, "#f2f2f2", "#736F6E")
                return True

        elif action == "color_mirror":
            if event.type() == QtCore.QEvent.HoverEnter:
                #self.animate.color_mirror(object, "rgba(0,0,0,0)", "#D3D3D3")
                return True
            if event.type() == QtCore.QEvent.HoverLeave:
                #self.animate.color_mirror(object, "#D3D3D3", "rgba(0,0,0,0)")
                return True

        elif action == "item_text":
            if event.type() == QtCore.QEvent.HoverEnter:
                object.setStyleSheet("color:red;")
                return True

        elif action == "context":
            if event.type() == QtCore.QEvent.ContextMenu:
                menu = QtWidgets.QMenu(self)
                menu.addAction(self.delete_icon, "Delete")

                if menu.exec_(event.globalPos()):
                    self.delete_session()
                return True

        return False
