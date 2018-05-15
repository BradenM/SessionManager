# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logo_item_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LogoItem(object):
    def setupUi(self, LogoItem):
        LogoItem.setObjectName("LogoItem")
        LogoItem.resize(400, 285)
        LogoItem.setStyleSheet("#logo_widget[empty=true]{\n"
"    background-color:rgba(27,27,27,0.5);\n"
"    border-radius:10px;\n"
"    border: 1px solid rgba(255,255,255,0.4);\n"
"    qproperty-cursor: 13;\n"
"}\n"
"\n"
"#logo_widget[empty=true] QLabel{\n"
"    color:rgba(255,255,255,0.4);\n"
"    background-color:rgba(0,0,0,0);\n"
"    font:35px \"Lato\";\n"
"}\n"
"\n"
"#logo_widget:hover{\n"
"    border-color:rgba(255,255,255,0.8);\n"
"    qproperty-cursor: 13;\n"
"}\n"
"\n"
"#logo_widget QLabel:hover{\n"
"    color:white;\n"
"}\n"
"")
        self.logo_widget = QtWidgets.QWidget(LogoItem)
        self.logo_widget.setGeometry(QtCore.QRect(0, 0, 140, 140))
        self.logo_widget.setMinimumSize(QtCore.QSize(140, 140))
        self.logo_widget.setMaximumSize(QtCore.QSize(140, 140))
        self.logo_widget.setProperty("empty", True)
        self.logo_widget.setObjectName("logo_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.logo_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.logo_img = QtWidgets.QLabel(self.logo_widget)
        self.logo_img.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_img.setObjectName("logo_img")
        self.gridLayout.addWidget(self.logo_img, 0, 0, 1, 1)

        self.retranslateUi(LogoItem)
        QtCore.QMetaObject.connectSlotsByName(LogoItem)

    def retranslateUi(self, LogoItem):
        _translate = QtCore.QCoreApplication.translate
        LogoItem.setWindowTitle(_translate("LogoItem", "Form"))
        self.logo_img.setText(_translate("LogoItem", "+"))

