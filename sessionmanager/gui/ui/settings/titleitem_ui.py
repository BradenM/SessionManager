# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'titleitem_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TitleItem(object):
    def setupUi(self, TitleItem):
        TitleItem.setObjectName("TitleItem")
        TitleItem.resize(510, 75)
        TitleItem.setStyleSheet("TitleItem{\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QLabel[title=true]{\n"
"    color:white;\n"
"    font: 24px \"Roboto\";\n"
"    font-weight:300;\n"
"}")
        self.widget = QtWidgets.QWidget(TitleItem)
        self.widget.setGeometry(QtCore.QRect(2, 2, 511, 70))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.title = QtWidgets.QLabel(self.widget)
        self.title.setMinimumSize(QtCore.QSize(311, 61))
        self.title.setMaximumSize(QtCore.QSize(311, 61))
        self.title.setProperty("title", True)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 1, 1, 1)
        self.logo = QtWidgets.QLabel(self.widget)
        self.logo.setMinimumSize(QtCore.QSize(24, 24))
        self.logo.setMaximumSize(QtCore.QSize(24, 24))
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 0, 0, 1, 1)

        self.retranslateUi(TitleItem)
        QtCore.QMetaObject.connectSlotsByName(TitleItem)

    def retranslateUi(self, TitleItem):
        _translate = QtCore.QCoreApplication.translate
        TitleItem.setWindowTitle(_translate("TitleItem", "Form"))
        self.title.setText(_translate("TitleItem", "TextLabel"))
        self.logo.setText(_translate("TitleItem", "logo"))

