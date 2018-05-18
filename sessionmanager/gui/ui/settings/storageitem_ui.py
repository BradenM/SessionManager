# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storageitem_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StorageItem(object):
    def setupUi(self, StorageItem):
        StorageItem.setObjectName("StorageItem")
        StorageItem.resize(510, 150)
        StorageItem.setStyleSheet("#setting_name{\n"
"    color:#f2f2f2;\n"
"    font: 18px \"Roboto\";\n"
"    font-weight:300;\n"
"}\n"
"\n"
"#setting_desc{\n"
"    color:gray;\n"
"    font:12px \"Lato\";\n"
"    font-weight:300;\n"
"}\n"
"\n"
"#setting_path{\n"
"    background-color:rgb(45,45,45);\n"
"    color:#f2f2f2;\n"
"    border:1px solid rgb(40,40,40);\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"#set_default{\n"
"    background-color:#323232;\n"
"    font: 14px \"Lato\";\n"
"    color:#f2f2f2;\n"
"}\n"
"\n"
"#set_default:hover{\n"
"    color:#1473e6;\n"
"    text-decoration:underline;\n"
"    background-color:#323232;\n"
"}")
        self.widget = QtWidgets.QWidget(StorageItem)
        self.widget.setGeometry(QtCore.QRect(13, 3, 272, 102))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.setting_name = QtWidgets.QLabel(self.widget)
        self.setting_name.setMinimumSize(QtCore.QSize(200, 40))
        self.setting_name.setMaximumSize(QtCore.QSize(200, 40))
        self.setting_name.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.setting_name.setObjectName("setting_name")
        self.verticalLayout.addWidget(self.setting_name)
        self.setting_desc = QtWidgets.QLabel(self.widget)
        self.setting_desc.setMinimumSize(QtCore.QSize(270, 60))
        self.setting_desc.setMaximumSize(QtCore.QSize(270, 40))
        self.setting_desc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.setting_desc.setObjectName("setting_desc")
        self.verticalLayout.addWidget(self.setting_desc)
        self.widget1 = QtWidgets.QWidget(StorageItem)
        self.widget1.setGeometry(QtCore.QRect(13, 105, 371, 42))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setting_path = QtWidgets.QLineEdit(self.widget1)
        self.setting_path.setMinimumSize(QtCore.QSize(280, 30))
        self.setting_path.setMaximumSize(QtCore.QSize(280, 30))
        self.setting_path.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setting_path.setFrame(False)
        self.setting_path.setClearButtonEnabled(False)
        self.setting_path.setObjectName("setting_path")
        self.horizontalLayout.addWidget(self.setting_path)
        self.setting_dir = QtWidgets.QToolButton(self.widget1)
        self.setting_dir.setMinimumSize(QtCore.QSize(25, 22))
        self.setting_dir.setMaximumSize(QtCore.QSize(25, 22))
        self.setting_dir.setProperty("dirOp", True)
        self.setting_dir.setObjectName("setting_dir")
        self.horizontalLayout.addWidget(self.setting_dir)
        self.set_default = QtWidgets.QPushButton(self.widget1)
        self.set_default.setMinimumSize(QtCore.QSize(40, 32))
        self.set_default.setMaximumSize(QtCore.QSize(40, 32))
        self.set_default.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_default.setFlat(True)
        self.set_default.setObjectName("set_default")
        self.horizontalLayout.addWidget(self.set_default)

        self.retranslateUi(StorageItem)
        QtCore.QMetaObject.connectSlotsByName(StorageItem)

    def retranslateUi(self, StorageItem):
        _translate = QtCore.QCoreApplication.translate
        StorageItem.setWindowTitle(_translate("StorageItem", "Form"))
        self.setting_name.setText(_translate("StorageItem", "Session Directory"))
        self.setting_desc.setText(_translate("StorageItem", "TextLabel"))
        self.setting_dir.setText(_translate("StorageItem", "..."))
        self.set_default.setText(_translate("StorageItem", "Reset"))

