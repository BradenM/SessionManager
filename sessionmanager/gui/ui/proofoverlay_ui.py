# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proofoverlay_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainOverlay(object):
    def setupUi(self, MainOverlay):
        MainOverlay.setObjectName("MainOverlay")
        MainOverlay.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainOverlay.sizePolicy().hasHeightForWidth())
        MainOverlay.setSizePolicy(sizePolicy)
        MainOverlay.setMinimumSize(QtCore.QSize(800, 600))
        MainOverlay.setMaximumSize(QtCore.QSize(800, 600))
        MainOverlay.setStyleSheet("QFrame{\n"
"    border:none;\n"
"}\n"
"\n"
"#proof_frame{\n"
"    background-color:rgba(27,27,27,0.5);\n"
"}\n"
"\n"
"#info_frame{\n"
"    background-color:rgba(27,27,27,0.9);\n"
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
        self.proof_frame = QtWidgets.QFrame(MainOverlay)
        self.proof_frame.setGeometry(QtCore.QRect(0, 0, 800, 430))
        self.proof_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.proof_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.proof_frame.setObjectName("proof_frame")
        self.layoutWidget = QtWidgets.QWidget(self.proof_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(400, 30, 391, 385))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setMaximumSize(QtCore.QSize(200, 20))
        self.label_2.setProperty("title", True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.proof = QtWidgets.QLabel(self.layoutWidget)
        self.proof.setMinimumSize(QtCore.QSize(350, 350))
        self.proof.setMaximumSize(QtCore.QSize(350, 350))
        self.proof.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.proof.setAlignment(QtCore.Qt.AlignCenter)
        self.proof.setProperty("Image", False)
        self.proof.setObjectName("proof")
        self.gridLayout_3.addWidget(self.proof, 1, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.proof_frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 31, 371, 385))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.loose_label = QtWidgets.QLabel(self.layoutWidget1)
        self.loose_label.setMinimumSize(QtCore.QSize(0, 25))
        self.loose_label.setMaximumSize(QtCore.QSize(200, 20))
        self.loose_label.setProperty("title", True)
        self.loose_label.setObjectName("loose_label")
        self.gridLayout_2.addWidget(self.loose_label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.loose_proof = QtWidgets.QLabel(self.layoutWidget1)
        self.loose_proof.setMinimumSize(QtCore.QSize(350, 350))
        self.loose_proof.setMaximumSize(QtCore.QSize(350, 350))
        self.loose_proof.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loose_proof.setAlignment(QtCore.Qt.AlignCenter)
        self.loose_proof.setProperty("Image", True)
        self.loose_proof.setObjectName("loose_proof")
        self.gridLayout_2.addWidget(self.loose_proof, 1, 0, 1, 1)
        self.close_button = QtWidgets.QLabel(self.proof_frame)
        self.close_button.setGeometry(QtCore.QRect(10, 7, 59, 20))
        self.close_button.setObjectName("close_button")
        self.info_frame = QtWidgets.QFrame(MainOverlay)
        self.info_frame.setGeometry(QtCore.QRect(0, 430, 800, 170))
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")
        self.image_name = QtWidgets.QLabel(self.info_frame)
        self.image_name.setGeometry(QtCore.QRect(210, 20, 109, 19))
        self.image_name.setMinimumSize(QtCore.QSize(91, 19))
        self.image_name.setMaximumSize(QtCore.QSize(109, 20))
        self.image_name.setAlignment(QtCore.Qt.AlignCenter)
        self.image_name.setObjectName("image_name")
        self.image = QtWidgets.QLabel(self.info_frame)
        self.image.setGeometry(QtCore.QRect(10, 10, 200, 150))
        self.image.setMinimumSize(QtCore.QSize(200, 150))
        self.image.setMaximumSize(QtCore.QSize(150, 150))
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.crop_box = QtWidgets.QGroupBox(self.info_frame)
        self.crop_box.setEnabled(True)
        self.crop_box.setGeometry(QtCore.QRect(570, 20, 221, 131))
        self.crop_box.setTitle("")
        self.crop_box.setProperty("img_edit", True)
        self.crop_box.setObjectName("crop_box")
        self.gridLayout = QtWidgets.QGridLayout(self.crop_box)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.crop_box)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        self.label_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.crop = QtWidgets.QComboBox(self.crop_box)
        self.crop.setMinimumSize(QtCore.QSize(0, 22))
        self.crop.setFrame(False)
        self.crop.setObjectName("crop")
        self.crop.addItem("")
        self.crop.addItem("")
        self.crop.addItem("")
        self.crop.addItem("")
        self.horizontalLayout.addWidget(self.crop)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.create = QtWidgets.QPushButton(self.crop_box)
        self.create.setMaximumSize(QtCore.QSize(170, 16777215))
        self.create.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create.setProperty("primary", True)
        self.create.setObjectName("create")
        self.gridLayout.addWidget(self.create, 1, 0, 1, 1)

        self.retranslateUi(MainOverlay)
        QtCore.QMetaObject.connectSlotsByName(MainOverlay)

    def retranslateUi(self, MainOverlay):
        _translate = QtCore.QCoreApplication.translate
        MainOverlay.setWindowTitle(_translate("MainOverlay", "Form"))
        self.label_2.setText(_translate("MainOverlay", "Proof"))
        self.proof.setToolTip(_translate("MainOverlay", "Add a proof"))
        self.proof.setText(_translate("MainOverlay", "+"))
        self.loose_label.setText(_translate("MainOverlay", "Loose Proof (5x7)"))
        self.loose_proof.setToolTip(_translate("MainOverlay", "Open in Preview"))
        self.loose_proof.setText(_translate("MainOverlay", "TextLabel"))
        self.close_button.setText(_translate("MainOverlay", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lato\'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">← <span style=\" font-size:16px;\">Back</span></p></body></html>"))
        self.image_name.setText(_translate("MainOverlay", "Image Name"))
        self.image.setText(_translate("MainOverlay", "image"))
        self.label_3.setText(_translate("MainOverlay", "Crop:"))
        self.crop.setItemText(0, _translate("MainOverlay", "5x7"))
        self.crop.setItemText(1, _translate("MainOverlay", "4x4"))
        self.crop.setItemText(2, _translate("MainOverlay", "Photoshop"))
        self.crop.setItemText(3, _translate("MainOverlay", "None"))
        self.create.setText(_translate("MainOverlay", "Create Proof"))

