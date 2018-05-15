# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logo_crop_overlay_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.widgets.photo_viewer import QPhotoView

class Ui_EditOverlay(object):
    def setupUi(self, EditOverlay):
        EditOverlay.setObjectName("EditOverlay")
        EditOverlay.resize(1200, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EditOverlay.sizePolicy().hasHeightForWidth())
        EditOverlay.setSizePolicy(sizePolicy)
        EditOverlay.setMinimumSize(QtCore.QSize(1200, 700))
        EditOverlay.setMaximumSize(QtCore.QSize(1200, 700))
        EditOverlay.setStyleSheet("#QFrame{\n"
"    border:none;\n"
"}\n"
"\n"
"#main_frame{\n"
"    background-color:rgba(96,96,96,1);\n"
"}\n"
"\n"
"#logo_frame{\n"
"    background-color:rgba(27,27,27,0.4);\n"
"    border-left: 1px solid #323232;\n"
"}\n"
"\n"
"#logo_list{\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"#edit_view{\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QLabel[title=true]{\n"
"    font: 20px \"Montserrat\";\n"
"}\n"
"\n"
"QLabel{\n"
"    color:white;\n"
"    background-color:rgba(0,0,0,0);\n"
"    font:16px \"Lato\";\n"
"}\n"
"\n"
"QLabel[Image=true]{\n"
"    padding:3px;\n"
"}\n"
"\n"
"QLabel[Image=true]:hover{\n"
"    border: 3px outset rgba(255,255,255,0.6);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QLabel[Image=false]{\n"
"    border: 3px outset rgba(255,255,255,0.3);\n"
"    border-radius: 5px;\n"
"    font: 30px;\n"
"    color: rgba(255,255,255,0.3);\n"
"}\n"
"\n"
"QLabel[Image=false]:hover{\n"
"    border: 3px outset rgba(255,255,255,0.9);\n"
"    color: white;\n"
"}\n"
"\n"
"QGroupBox[img_edit=true]{\n"
"    border: 1px solid rgba(255,255,255,0.3);\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QPushButton[primary=true]{\n"
"    color:white;\n"
"    background-color:#1473e6;\n"
"    border-style:solid;\n"
"    border-width:2px;\n"
"    border-radius:14px;\n"
"    border-color:#1473e6;\n"
"    padding:6 18 6 18px;\n"
"    font:16pt \"Roboto\";\n"
"}\n"
"")
        self.main_frame = QtWidgets.QFrame(EditOverlay)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.edit_view = QPhotoView(self.main_frame)
        self.edit_view.setGeometry(QtCore.QRect(0, 0, 1010, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_view.sizePolicy().hasHeightForWidth())
        self.edit_view.setSizePolicy(sizePolicy)
        self.edit_view.setMinimumSize(QtCore.QSize(1010, 700))
        self.edit_view.setMaximumSize(QtCore.QSize(600, 600))
        self.edit_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.edit_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.edit_view.setObjectName("edit_view")
        self.logo_frame = QtWidgets.QFrame(self.main_frame)
        self.logo_frame.setGeometry(QtCore.QRect(1010, 0, 190, 700))
        self.logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_frame.setObjectName("logo_frame")
        self.logo_list = QtWidgets.QListWidget(self.logo_frame)
        self.logo_list.setGeometry(QtCore.QRect(2, 50, 185, 645))
        self.logo_list.setMinimumSize(QtCore.QSize(185, 645))
        self.logo_list.setMaximumSize(QtCore.QSize(185, 645))
        self.logo_list.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo_list.setDragEnabled(True)
        self.logo_list.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.logo_list.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.logo_list.setGridSize(QtCore.QSize(140, 150))
        self.logo_list.setObjectName("logo_list")
        self.label = QtWidgets.QLabel(self.logo_frame)
        self.label.setGeometry(QtCore.QRect(35, 0, 120, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setProperty("title", True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.logo_list.raise_()
        self.logo_frame.raise_()
        self.edit_view.raise_()

        self.retranslateUi(EditOverlay)
        QtCore.QMetaObject.connectSlotsByName(EditOverlay)

    def retranslateUi(self, EditOverlay):
        _translate = QtCore.QCoreApplication.translate
        EditOverlay.setWindowTitle(_translate("EditOverlay", "Form"))
        self.label.setText(_translate("EditOverlay", "Logos"))

