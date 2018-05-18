# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generalitem_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GeneralItem(object):
    def setupUi(self, GeneralItem):
        GeneralItem.setObjectName("GeneralItem")
        GeneralItem.resize(510, 150)
        GeneralItem.setStyleSheet("#setting_name{\n"
"    color:#f2f2f2;\n"
"    font: 18px \"Roboto\";\n"
"    font-weight:300;\n"
"}\n"
"\n"
"#setting_desc{\n"
"    color:gray;\n"
"    font:12px \"Lato\";\n"
"    font-weight:300;\n"
"    margin-left:20;\n"
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
        self.widget = QtWidgets.QWidget(GeneralItem)
        self.widget.setGeometry(QtCore.QRect(3, 5, 221, 47))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setting_state = QtWidgets.QCheckBox(self.widget)
        self.setting_state.setMaximumSize(QtCore.QSize(20, 16777215))
        self.setting_state.setText("")
        self.setting_state.setObjectName("setting_state")
        self.horizontalLayout.addWidget(self.setting_state)
        self.setting_name = QtWidgets.QLabel(self.widget)
        self.setting_name.setMinimumSize(QtCore.QSize(200, 40))
        self.setting_name.setMaximumSize(QtCore.QSize(200, 40))
        self.setting_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.setting_name.setObjectName("setting_name")
        self.horizontalLayout.addWidget(self.setting_name)
        self.setting_desc = QtWidgets.QLabel(GeneralItem)
        self.setting_desc.setGeometry(QtCore.QRect(3, 40, 240, 50))
        self.setting_desc.setMinimumSize(QtCore.QSize(240, 50))
        self.setting_desc.setMaximumSize(QtCore.QSize(240, 50))
        self.setting_desc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.setting_desc.setWordWrap(False)
        self.setting_desc.setObjectName("setting_desc")

        self.retranslateUi(GeneralItem)
        QtCore.QMetaObject.connectSlotsByName(GeneralItem)

    def retranslateUi(self, GeneralItem):
        _translate = QtCore.QCoreApplication.translate
        GeneralItem.setWindowTitle(_translate("GeneralItem", "Form"))
        self.setting_name.setText(_translate("GeneralItem", "Session Directory"))
        self.setting_desc.setText(_translate("GeneralItem", "TextLabel"))

