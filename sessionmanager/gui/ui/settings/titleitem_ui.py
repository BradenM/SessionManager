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
"QLabel[stitle=true]{\n"
"    color:#f2f2f2;\n"
"    font: 32px \"Lato\";\n"
"    font-weight:900;\n"
"}")
        self.layoutWidget = QtWidgets.QWidget(TitleItem)
        self.layoutWidget.setGeometry(QtCore.QRect(2, 2, 420, 70))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.logo = QtWidgets.QLabel(self.layoutWidget)
        self.logo.setMinimumSize(QtCore.QSize(32, 32))
        self.logo.setMaximumSize(QtCore.QSize(32, 32))
        self.logo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 0, 0, 1, 1)
        self.setting_title = QtWidgets.QLabel(self.layoutWidget)
        self.setting_title.setMinimumSize(QtCore.QSize(311, 61))
        self.setting_title.setMaximumSize(QtCore.QSize(311, 61))
        self.setting_title.setProperty("stitle", True)
        self.setting_title.setObjectName("setting_title")
        self.gridLayout.addWidget(self.setting_title, 0, 1, 1, 1)
        self.close_button = QtWidgets.QLabel(TitleItem)
        self.close_button.setGeometry(QtCore.QRect(360, 10, 150, 20))
        self.close_button.setMinimumSize(QtCore.QSize(150, 20))
        self.close_button.setMaximumSize(QtCore.QSize(150, 20))
        self.close_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_button.setAlignment(QtCore.Qt.AlignCenter)
        self.close_button.setProperty("close_button", True)
        self.close_button.setObjectName("close_button")

        self.retranslateUi(TitleItem)
        QtCore.QMetaObject.connectSlotsByName(TitleItem)

    def retranslateUi(self, TitleItem):
        _translate = QtCore.QCoreApplication.translate
        TitleItem.setWindowTitle(_translate("TitleItem", "Form"))
        self.logo.setText(_translate("TitleItem", "logo"))
        self.setting_title.setText(_translate("TitleItem", "TextLabel"))
        self.close_button.setText(_translate("TitleItem", "X  Close"))

