# Program: Session Manager
# File: gui/dialogs/settings_mod.py
# Desc: Setting Window Module
# Author: Braden Mars

from gui.ui.settings.settings_ui import Ui_SettingsModule
from gui.ui.settings.titleitem_ui import Ui_TitleItem
from PyQt5 import QtCore, QtGui, QtWidgets
import qtawesome as fa


class SettingTitle(QtWidgets.QWidget):
    def __init__(self, parent):
        super(SettingTitle, self).__init__(parent)
        self.ui = Ui_TitleItem()
        self.ui.setupUi(self)
        self.title_icon = fa.icon('fa.code', color="white")

    def load(self):
        self.ui.title.setText("Test Title")
        self.ui.logo.setText(fa.charmap('fa.home'))


class SettingsModule(QtWidgets.QWidget):
    def __init__(self, parent):
        super(SettingsModule, self).__init__(parent)
        self.ui = Ui_SettingsModule()
        self.ui.setupUi(self)

        # Vars

        # Connections

        # Setup
        print('settings loaded')
        self.test()

    # Functions
    def test(self):
        title_item = SettingTitle(self)
        title_item.load()
        item = QtWidgets.QListWidgetItem(self.ui.setting_list)
        item.setSizeHint(title_item.size())
        self.ui.setting_list.addItem(item)
        self.ui.setting_list.setItemWidget(item, title_item)
