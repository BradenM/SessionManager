# Program: Session Manger
# File: gui/widgets/image_item.py
# Desc: Overlay for opened photos
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.image_item_ui import Ui_ImageItem
from definitions import ROOT_DIR
from gui import gui_handle as handle


class QImageItem(QtWidgets.QWidget):
    def __init__(self, img, overlay=False):
        super(QImageItem, self).__init__()
        self.ui = Ui_ImageItem()
        self.ui.setupUi(self)
        self.img = img
        self.ui.overlay.hide()
        self.ui.image.setStyleSheet('''
            background-color:rgba(0,0,0,0);
            border-left:4px solid rgba(0,0,0,0);
            border-right:4px solid rgba(0,0,0,0);
        ''')
        self.set_image()
        if overlay:
            self.overlay()

    def set_image(self):
        icon = QtGui.QPixmap(self.img.thumb).scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.ui.image.setPixmap(icon)

    def overlay(self):
        blur = QtWidgets.QGraphicsBlurEffect()
        blur.setBlurRadius(6)
        self.ui.image_widget.setGraphicsEffect(blur)
        self.ui.overlay.show()
        icon = QtGui.QPixmap(f"{ROOT_DIR}/icons/ps.png").scaled(64,64, QtCore.Qt.KeepAspectRatio)
        self.ui.overlay_icon.setPixmap(icon)
