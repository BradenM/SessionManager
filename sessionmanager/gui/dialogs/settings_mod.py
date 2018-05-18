# Program: Session Manager
# File: gui/dialogs/settings_mod.py
# Desc: Setting Window Module
# Author: Braden Mars

from gui.ui.settings.settings_ui import Ui_SettingsModule
from gui.ui.settings.titleitem_ui import Ui_TitleItem
from gui.ui.settings.tabitem_ui import Ui_TabItem
from gui.ui.settings.storageitem_ui import Ui_StorageItem
from gui.ui.settings.generalitem_ui import Ui_GeneralItem
from manage.settings import Setting
from manage.session import Session
from gui import gui_handle as handle
from PyQt5 import QtCore, QtGui, QtWidgets
from definitions import ICONS
import qtawesome as fa
from functools import partial


class SettingTab(QtWidgets.QWidget):
    def __init__(self, parent, title, pix):
        super(SettingTab, self).__init__(parent)
        self.ui = Ui_TabItem()
        self.ui.setupUi(self)
        # Vars
        self.title = title
        self.pix = pix

    def load(self):
        self.ui.tab_title.setText(self.title)
        self.ui.tab_icon.setPixmap(self.pix)


class SettingTitle(QtWidgets.QWidget):
    def __init__(self, parent, title, pixmap):
        super(SettingTitle, self).__init__(parent)
        self.ui = Ui_TitleItem()
        self.ui.setupUi(self)
        # Vars
        self.parent = parent
        self.title = title
        self.icon = pixmap
        # Connections
        self.ui.close_button.mousePressEvent = self.close

    def load(self):
        self.ui.setting_title.setText(self.title)
        self.ui.logo.setPixmap(self.icon)

    def close(self, e):
        self.parent.close()


class SettingStorage(QtWidgets.QWidget):
    def __init__(self, parent, inst):
        super(SettingStorage, self).__init__(parent)
        self.ui = Ui_StorageItem()
        self.ui.setupUi(self)
        # Vars
        self.inst = inst
        self.name = inst.name
        self.desc = inst.desc
        self.path = inst.path
        self.default = inst.default
        self.open_icon = fa.icon('fa.folder', color='gray')
        # Setup
        self.ui.setting_dir.setIcon(self.open_icon)
        self.ui.setting_desc.setWordWrap(True)
        self.ui.setting_desc.setMinimumSize(self.ui.setting_desc.sizeHint())
        # Connections
        self.ui.setting_dir.clicked.connect(self.modify)
        self.ui.set_default.clicked.connect(self.reset)

    def load(self):
        self.ui.setting_name.setText(self.name)
        self.ui.setting_desc.setText(self.desc)
        self.ui.setting_path.setPlaceholderText(self.path)
        self.ui.setting_path.setToolTip(self.path)

    def modify(self):
        dialog = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select a Directory"))
        path = f"{dialog}/SessionManager/sessions"
        origin = Session.__dir__
        if self.inst.migrate(origin, path):
            Session().update_migration(origin, path)
            self.ui.setting_path.setText(path)
        else:
            pass

    def reset(self):
        self.ui.setting_path.setText(self.default)


class SettingGeneral(QtWidgets.QWidget):
    def __init__(self, parent, inst):
        super(SettingGeneral, self).__init__(parent)
        self.ui = Ui_GeneralItem()
        self.ui.setupUi(self)
        # Vars
        self.name = inst.name
        self.desc = inst.desc
        self.state = inst.state
        print(f"STATE: {self.state}")
        # Setup
        self.ui.setting_desc.setWordWrap(True)
        self.ui.setting_desc.setMinimumSize(self.ui.setting_desc.sizeHint())

    def load(self):
        self.ui.setting_name.setText(self.name)
        self.ui.setting_desc.setText(self.desc)
        self.ui.setting_state.setChecked(self.state)


class SettingsModule(QtWidgets.QWidget):
    def __init__(self, parent):
        super(SettingsModule, self).__init__(parent)
        self.ui = Ui_SettingsModule()
        self.ui.setupUi(self)

        # Vars
        self.setting = Setting
        self.general = handle.get_settings(self.setting)[0]
        self.storage = handle.get_settings(self.setting)[1]
        self.tabs = [self.general, self.storage]

        # Connections
        self.ui.setting_tab.itemClicked.connect(self.load_window)

        # Setup
        print('settings loaded')
        self.ui.setting_list.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.ui.setting_tab.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.load_tabs()

    # Functions
    def active(self):
        tab = self.ui.setting_tab.currentItem().data(QtCore.Qt.UserRole)
        return tab

    def load_tabs(self):
        for cat in self.tabs:
            pix = QtGui.QPixmap(cat[0].__icon__).scaled(24, 24, QtCore.Qt.KeepAspectRatio)
            tab = SettingTab(self, cat[0].__tab__, pix)
            tab.load()
            item = QtWidgets.QListWidgetItem(self.ui.setting_tab)
            item.setData(QtCore.Qt.UserRole, cat)
            item.setSizeHint(tab.size())
            self.ui.setting_tab.addItem(item)
            self.ui.setting_tab.setItemWidget(item, tab)
            print(f'DATA ==> {cat}')
        self.ui.setting_tab.setCurrentItem(self.ui.setting_tab.item(0))
        self.load_window()

    def load_window(self):
        self.ui.setting_list.clear()
        tab = self.active()
        pix = QtGui.QPixmap(tab[0].__winicon__).scaled(32, 32, QtCore.Qt.KeepAspectRatio)
        title_item = SettingTitle(self, tab[0].__tab__, pix)
        title_item.load()
        item = QtWidgets.QListWidgetItem(self.ui.setting_list)
        item.setSizeHint(title_item.size())
        self.ui.setting_list.addItem(item)
        self.ui.setting_list.setItemWidget(item, title_item)
        self.load_settings(tab)

    def load_settings(self, tab):
        for s in tab:
            if s.type == "storage":
                widg = SettingStorage(self, s)
            elif s.type == "general":
                widg = SettingGeneral(self, s)
            widg.load()
            item = QtWidgets.QListWidgetItem(self.ui.setting_list)
            item.setSizeHint(widg.size())
            self.ui.setting_list.addItem(item)
            self.ui.setting_list.setItemWidget(item, widg)

    def close(self):
        self.setVisible(False)