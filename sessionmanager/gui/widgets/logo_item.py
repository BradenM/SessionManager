# Program: Session Manager
# File: gui/widgets/logo_item.py
# Desc: Logo Item Widget
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.logo_item_ui import Ui_LogoItem
from gui.widgets.event_filter import EventFilter


class QLogoItem(QtWidgets.QWidget):
    def __init__(self, logo=None):
        super(QLogoItem, self).__init__()
        self.ui = Ui_LogoItem()
        self.ui.setupUi(self)
        # Vars
        self.filter = EventFilter(self)
        self.installEventFilter(self.filter)
        self.setProperty("action", "drop")
        self.logo = logo
        if self.logo is not None:
            self.set_logo()

    def set_logo(self):
        icon = QtGui.QPixmap(self.logo.thumb).scaled(130, 130, QtCore.Qt.KeepAspectRatio)
        self.ui.logo_img.setPixmap(icon)


