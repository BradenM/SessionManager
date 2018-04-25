# Program: Session Manager
# File: gui/ui/imageitem.py
# Desc: Image item widget
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets


class QImageItem(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(QImageItem, self).__init__(parent)
        self.setGeometry(0,0,182,220)

        self.ImageItem = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon = QtWidgets.QLabel()
        self.name = QtWidgets.QLabel()
        self.date = QtWidgets.QLabel()
        self.ImageItem.addWidget(self.icon)
        self.ImageItem.addWidget(self.icon)
        self.ImageItem.addWidget(self.icon)
        self.setLayout(self.ImageItem)

    def set_icon(self, path):
            self.icon.setPixmap(QtGui.QPixmap(path).scaled(180, 180, QtCore.Qt.KeepAspectRatio))

    def set_name(self, text):
        self.name.setText(text)

    def set_date(self, text):
        self.date.setText(text)
