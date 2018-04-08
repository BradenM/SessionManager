# Program: Session Manager
# File: gui/dialog/popup
# Desc: Popup windows
# Author: Braden Mars

from gui.ui.popup_ui import Ui_popup
from PyQt5 import QtWidgets

class Popup(QtWidgets.QDialog):
    def __init__(self):
        super(Popup, self).__init__()
        self.ui = Ui_popup()
        self.ui.setupUi(self)
