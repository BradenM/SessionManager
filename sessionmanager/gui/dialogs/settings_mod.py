# Program: Session Manager
# File: gui/dialogs/settings_mod.py
# Desc: Setting Window Module
# Author: Braden Mars

from gui.ui.settings.settings_ui import Ui_SettingsModule
from gui.ui.settings.titleitem_ui import Ui_TitleItem
from gui.ui.settings.tabitem_ui import Ui_TabItem
from gui.ui.settings.storageitem_ui import Ui_StorageItem
from manage.settings import Setting, DEFAULT
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
        self.title = title
        self.icon = pixmap

    def load(self):
        self.ui.setting_title.setText(self.title)
        self.ui.logo.setPixmap(self.icon)


class SettingStorage(QtWidgets.QWidget):
    def __init__(self, parent, name, desc, path):
        super(SettingStorage, self).__init__(parent)
        self.ui = Ui_StorageItem()
        self.ui.setupUi(self)
        # Vars
        self.name = name
        self.desc = desc
        self.path = path
        self.open_icon = fa.icon('fa.folder', color='gray')
        # Connections
        #self.ui.setting_dir.clicked.connect(self.test)

        # Setup
        self.ui.setting_dir.setIcon(self.open_icon)

    def load(self):
        self.ui.setting_name.setText(self.name)
        self.ui.setting_desc.setText(self.desc)
        self.ui.setting_path.setPlaceholderText(self.path)
        self.ui.setting_path.setToolTip(self.path)


class SettingsModule(QtWidgets.QWidget):
    def __init__(self, parent):
        super(SettingsModule, self).__init__(parent)
        self.ui = Ui_SettingsModule()
        self.ui.setupUi(self)

        # Vars
        self.setting = Setting
        self.general = handle.get_settings(self.setting)[0]
        self.storage = handle.get_settings(self.setting)[1]

        # Connections
        #self.ui.setting_tab.itemClicked()

        # Setup
        print('settings loaded')
        self.ui.setting_list.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.ui.setting_tab.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.load_tabs()
        self.load_window()
        self.load_settings()

    # Functions
    def load_tabs(self):
            pix = QtGui.QPixmap(f'{ICONS}/settings/gen.png').scaled(24, 24, QtCore.Qt.KeepAspectRatio)
            tab = SettingTab(self, "General", pix)
            tab.load()
            item = QtWidgets.QListWidgetItem(self.ui.setting_tab)
            item.setSizeHint(tab.size())
            self.ui.setting_tab.addItem(item)
            self.ui.setting_tab.setItemWidget(item, tab)

    def load_window(self):
        pix = QtGui.QPixmap(f"{ICONS}/settings/gen_title.png").scaled(32, 32, QtCore.Qt.KeepAspectRatio)
        title_item = SettingTitle(self, "General", pix)
        title_item.load()
        item = QtWidgets.QListWidgetItem(self.ui.setting_list)
        item.setSizeHint(title_item.size())
        self.ui.setting_list.addItem(item)
        self.ui.setting_list.setItemWidget(item, title_item)

    def load_settings(self):
        for x in self.storage:
            storage = SettingStorage(self, x.name, x.desc, x.path)
            storage.load()
            item = QtWidgets.QListWidgetItem(self.ui.setting_list)
            item.setSizeHint(storage.size())
            self.ui.setting_list.addItem(item)
            self.ui.setting_list.setItemWidget(item, storage)
