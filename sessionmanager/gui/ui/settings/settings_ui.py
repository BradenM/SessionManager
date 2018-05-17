# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsModule(object):
    def setupUi(self, SettingsModule):
        SettingsModule.setObjectName("SettingsModule")
        SettingsModule.setWindowModality(QtCore.Qt.WindowModal)
        SettingsModule.resize(800, 600)
        SettingsModule.setMinimumSize(QtCore.QSize(800, 600))
        SettingsModule.setMaximumSize(QtCore.QSize(800, 600))
        SettingsModule.setStyleSheet("#SettingsModule{\n"
"    background-color:black;\n"
"}\n"
"\n"
"QLabel[title=true]{\n"
"    color:white;\n"
"    font: 24px \"Roboto\";\n"
"    font-weight:300;\n"
"}\n"
"\n"
"#module{\n"
"    background-color:#464646;\n"
"    border-color:2px solid black;\n"
"}\n"
"\n"
"#setting_tab{\n"
"    background-color:rgba(0,0,0,0);\n"
"    border-right:1px solid #151515;\n"
"}\n"
"\n"
"#setting_list,\n"
"#setting_view{\n"
"    background-color:rgba(0,0,0,0);\n"
"    border:none !important;\n"
"    \n"
"}\n"
"")
        self.module = QtWidgets.QFrame(SettingsModule)
        self.module.setGeometry(QtCore.QRect(50, 65, 700, 500))
        self.module.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.module.setFrameShadow(QtWidgets.QFrame.Raised)
        self.module.setObjectName("module")
        self.setting_tab = QtWidgets.QListView(self.module)
        self.setting_tab.setGeometry(QtCore.QRect(0, 0, 190, 501))
        self.setting_tab.setObjectName("setting_tab")
        self.setting_view = QtWidgets.QWidget(self.module)
        self.setting_view.setGeometry(QtCore.QRect(190, 0, 510, 500))
        self.setting_view.setObjectName("setting_view")
        self.setting_list = QtWidgets.QListWidget(self.setting_view)
        self.setting_list.setGeometry(QtCore.QRect(0, 0, 510, 500))
        self.setting_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.setting_list.setObjectName("setting_list")

        self.retranslateUi(SettingsModule)
        QtCore.QMetaObject.connectSlotsByName(SettingsModule)

    def retranslateUi(self, SettingsModule):
        _translate = QtCore.QCoreApplication.translate
        SettingsModule.setWindowTitle(_translate("SettingsModule", "Form"))

