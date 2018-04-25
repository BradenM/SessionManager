# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sessionitem_widget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(200, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QtCore.QSize(200, 200))
        Widget.setMaximumSize(QtCore.QSize(200, 200))
        Widget.setStyleSheet("#SessionItem{\n"
"    background-color:#323232;\n"
"    border:1px solid #151515;\n"
"    border-radius: 5px;\n"
"    color:#f2f2f2;\n"
"}\n"
"\n"
"#SessionItem:hover{\n"
"    color:#1473e6;\n"
"    background-color:#282828;\n"
"    cursor:pointer;\n"
"    outline:none;\n"
"}\n"
"\n"
"#SessionItem:selected{\n"
"    border:1px solid #1473e6;\n"
"    border-radius: 5px;\n"
"    outline:none;\n"
"}\n"
"\n"
"QAbstractItemView:selected{\n"
"    outline:none;\n"
"    color:none;\n"
"}\n"
"\n"
"#icon{\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"#name{\n"
"    background-color:rgba(0,0,0,0);\n"
"    font: 10pt \"Montserrat\";\n"
"    color:#f2f2f2;\n"
"}")
        self.SessionItem = QtWidgets.QFrame(Widget)
        self.SessionItem.setGeometry(QtCore.QRect(-1, 0, 201, 201))
        self.SessionItem.setMinimumSize(QtCore.QSize(201, 201))
        self.SessionItem.setMaximumSize(QtCore.QSize(201, 201))
        self.SessionItem.setStyleSheet("#SessionItem{\n"
"    background-color:#323232;\n"
"    border:1px solid #151515;\n"
"    border-radius: 5px;\n"
"    color:#f2f2f2;\n"
"}\n"
"\n"
"#SessionItem:hover{\n"
"    color:#1473e6;\n"
"    background-color:#282828;\n"
"    cursor:pointer;\n"
"    outline:none;\n"
"}\n"
"\n"
"#SessionItem:selected{\n"
"    border:1px solid #1473e6;\n"
"    border-radius: 5px;\n"
"    outline:none;\n"
"}\n"
"\n"
"QAbstractItemView:selected{\n"
"    outline:none;\n"
"    color:none;\n"
"}\n"
"\n"
"#icon{\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"#name{\n"
"    background-color:rgba(0,0,0,0);\n"
"    font: 10pt \"Montserrat\";\n"
"}")
        self.SessionItem.setObjectName("SessionItem")
        self.grid = QtWidgets.QGridLayout(self.SessionItem)
        self.grid.setObjectName("grid")
        self.icon = QtWidgets.QLabel(self.SessionItem)
        self.icon.setMinimumSize(QtCore.QSize(199, 97))
        self.icon.setMaximumSize(QtCore.QSize(199, 97))
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.icon.setObjectName("icon")
        self.grid.addWidget(self.icon, 0, 0, 1, 1)
        self.name = QtWidgets.QLabel(self.SessionItem)
        self.name.setMinimumSize(QtCore.QSize(199, 96))
        self.name.setMaximumSize(QtCore.QSize(199, 96))
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setWordWrap(True)
        self.name.setObjectName("name")
        self.grid.addWidget(self.name, 1, 0, 1, 1)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Form"))
        self.icon.setText(_translate("Widget", "TextLabel"))
        self.name.setText(_translate("Widget", "TextLabel"))

