# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabitem_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabItem(object):
    def setupUi(self, TabItem):
        TabItem.setObjectName("TabItem")
        TabItem.resize(160, 60)
        TabItem.setMaximumSize(QtCore.QSize(189, 60))
        TabItem.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        TabItem.setStyleSheet("#TabItem{\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"#tab_title{\n"
"    font: 20px \"Lato\";\n"
"    color:#C0C0C0;\n"
"}")
        self.layoutWidget = QtWidgets.QWidget(TabItem)
        self.layoutWidget.setGeometry(QtCore.QRect(4, 3, 150, 52))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tab_icon = QtWidgets.QLabel(self.layoutWidget)
        self.tab_icon.setMinimumSize(QtCore.QSize(24, 24))
        self.tab_icon.setMaximumSize(QtCore.QSize(24, 24))
        self.tab_icon.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tab_icon.setObjectName("tab_icon")
        self.horizontalLayout.addWidget(self.tab_icon)
        self.tab_title = QtWidgets.QLabel(self.layoutWidget)
        self.tab_title.setMinimumSize(QtCore.QSize(105, 50))
        self.tab_title.setMaximumSize(QtCore.QSize(105, 50))
        self.tab_title.setObjectName("tab_title")
        self.horizontalLayout.addWidget(self.tab_title)

        self.retranslateUi(TabItem)
        QtCore.QMetaObject.connectSlotsByName(TabItem)

    def retranslateUi(self, TabItem):
        _translate = QtCore.QCoreApplication.translate
        TabItem.setWindowTitle(_translate("TabItem", "Form"))
        self.tab_icon.setText(_translate("TabItem", "log"))
        self.tab_title.setText(_translate("TabItem", "General"))

