# Program: SessionManager
# File: gui/widgets/sessionitem.py
# Desc: Session Item widget
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets


class QSessionItem(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(QSessionItem, self).__init__(parent)
        self.setGeometry(0,0,160,160)
        font_db = QtGui.QFontDatabase()
        font_db.addApplicationFont("gui/ui/assets/fonts/Roboto-Light.ttf")

        self.SessionItem = QtWidgets.QGridLayout()
        #self.SessionItem.setGeometry(200)
        self.SessionItem.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.SessionItem.setContentsMargins(0, 0, 0, 0)
        self.icon = QtWidgets.QLabel()
        #self.icon.setMinimumSize(QtCore.QSize(200, 100))
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.name = QtWidgets.QLabel()
        #self.name.setMinimumSize(QtCore.QSize(200, 100))
        self.name.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.SessionItem.addWidget(self.icon)
        self.SessionItem.addWidget(self.name)
        self.setLayout(self.SessionItem)

        self.icon.setStyleSheet('''
            background-color:rgba(0,0,0,0);
            padding-top:40px;
        ''')

        self.name.setStyleSheet('''
            background-color:rgba(0,0,0,0);
            font-size: 12pt;
            font-family: "Roboto";
            color:#f2f2f2;
        ''')

    def set_name(self, text):
        self.name.setText(text)

    def set_icon(self, path):
        self.icon.setPixmap(QtGui.QPixmap(path).scaled(60, 60, QtCore.Qt.KeepAspectRatio))
