# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_preview_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImagePreview(object):
    def setupUi(self, ImagePreview):
        ImagePreview.setObjectName("ImagePreview")
        ImagePreview.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ImagePreview.sizePolicy().hasHeightForWidth())
        ImagePreview.setSizePolicy(sizePolicy)
        ImagePreview.setMinimumSize(QtCore.QSize(800, 600))
        ImagePreview.setMaximumSize(QtCore.QSize(800, 600))
        ImagePreview.setWindowOpacity(1.0)
        ImagePreview.setAutoFillBackground(False)
        ImagePreview.setStyleSheet("QWidget{\n"
"    background:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QFrame{\n"
"    border:none;\n"
"}\n"
"\n"
"#preview_frame{\n"
"    background-color:rgba(27,27,27,0.5);\n"
"}\n"
"\n"
"#slider_frame{\n"
"    background-color:rgba(27,27,27,0.9);\n"
"}\n"
"\n"
"#slider::item{\n"
"    border:4px solid rgba(0,0,0,0);\n"
"    border-radius: 5px;\n"
"    padding:0px;\n"
"}\n"
"\n"
"#slider::item:selected{\n"
"    border-color:#f2f2f2;\n"
"    outline:none;\n"
"}\n"
"\n"
"QLabel{\n"
"    color:white;\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"#close_overlay{\n"
"color:#f2f2f2;\n"
"font:15pt \"Lato\";\n"
"font-weight:900;\n"
"}\n"
"\n"
"QAbstractItemView:selected{\n"
"    outline:none;\n"
"    color:none;\n"
"}\n"
"\n"
"#add_image{\n"
"    color:white;\n"
"    background-color:#1473e6;\n"
"    border-style:solid;\n"
"    border-width:2px;\n"
"    border-radius:14px;\n"
"    border-color:#1473e6;\n"
"    padding:6 8 6 8px;\n"
"    font:16pt \"Roboto\";\n"
"    \n"
"}\n"
"\n"
"#add_image:disabled{\n"
"    background-color:gray;\n"
"    border-color:gray;\n"
"}\n"
"")
        self.preview_frame = QtWidgets.QFrame(ImagePreview)
        self.preview_frame.setGeometry(QtCore.QRect(0, 0, 800, 470))
        self.preview_frame.setStyleSheet("")
        self.preview_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.preview_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.preview_frame.setObjectName("preview_frame")
        self.image_frame = QtWidgets.QFrame(self.preview_frame)
        self.image_frame.setGeometry(QtCore.QRect(0, 0, 800, 450))
        self.image_frame.setObjectName("image_frame")
        self.preview_image = QtWidgets.QLabel(self.image_frame)
        self.preview_image.setGeometry(QtCore.QRect(160, 10, 500, 450))
        self.preview_image.setMinimumSize(QtCore.QSize(500, 450))
        self.preview_image.setMaximumSize(QtCore.QSize(500, 450))
        self.preview_image.setStyleSheet("color:#f2f2f2;\n"
"font:20pt \"Lato\";\n"
"font-weight:900;\n"
"")
        self.preview_image.setAlignment(QtCore.Qt.AlignCenter)
        self.preview_image.setObjectName("preview_image")
        self.close_overlay = QtWidgets.QPushButton(self.image_frame)
        self.close_overlay.setGeometry(QtCore.QRect(700, 40, 40, 40))
        self.close_overlay.setMinimumSize(QtCore.QSize(40, 40))
        self.close_overlay.setMaximumSize(QtCore.QSize(40, 40))
        self.close_overlay.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_overlay.setAutoDefault(False)
        self.close_overlay.setFlat(True)
        self.close_overlay.setObjectName("close_overlay")
        self.label = QtWidgets.QLabel(self.image_frame)
        self.label.setGeometry(QtCore.QRect(20, 225, 22, 31))
        self.label.setMaximumSize(QtCore.QSize(50, 50))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.image_frame)
        self.label_2.setGeometry(QtCore.QRect(750, 225, 22, 31))
        self.label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.slider_frame = QtWidgets.QFrame(ImagePreview)
        self.slider_frame.setGeometry(QtCore.QRect(0, 470, 800, 130))
        self.slider_frame.setStyleSheet("")
        self.slider_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slider_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slider_frame.setObjectName("slider_frame")
        self.slider = QtWidgets.QListWidget(self.slider_frame)
        self.slider.setGeometry(QtCore.QRect(11, 11, 630, 110))
        self.slider.setMinimumSize(QtCore.QSize(630, 110))
        self.slider.setMaximumSize(QtCore.QSize(630, 110))
        self.slider.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.slider.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.slider.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.slider.setProperty("showDropIndicator", False)
        self.slider.setMovement(QtWidgets.QListView.Static)
        self.slider.setFlow(QtWidgets.QListView.LeftToRight)
        self.slider.setProperty("isWrapping", False)
        self.slider.setViewMode(QtWidgets.QListView.IconMode)
        self.slider.setObjectName("slider")
        self.info = QtWidgets.QGroupBox(self.slider_frame)
        self.info.setGeometry(QtCore.QRect(650, -2, 141, 111))
        self.info.setMinimumSize(QtCore.QSize(141, 111))
        self.info.setMaximumSize(QtCore.QSize(141, 111))
        self.info.setTitle("")
        self.info.setFlat(False)
        self.info.setObjectName("info")
        self.widget = QtWidgets.QWidget(self.info)
        self.widget.setGeometry(QtCore.QRect(20, 20, 100, 67))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.file_name = QtWidgets.QLabel(self.widget)
        self.file_name.setText("")
        self.file_name.setAlignment(QtCore.Qt.AlignCenter)
        self.file_name.setObjectName("file_name")
        self.verticalLayout.addWidget(self.file_name)
        self.add_image = QtWidgets.QPushButton(self.widget)
        self.add_image.setEnabled(False)
        self.add_image.setObjectName("add_image")
        self.verticalLayout.addWidget(self.add_image)

        self.retranslateUi(ImagePreview)
        QtCore.QMetaObject.connectSlotsByName(ImagePreview)

    def retranslateUi(self, ImagePreview):
        _translate = QtCore.QCoreApplication.translate
        ImagePreview.setWindowTitle(_translate("ImagePreview", "Form"))
        self.preview_image.setText(_translate("ImagePreview", "Select a Photo to Preview"))
        self.close_overlay.setText(_translate("ImagePreview", "X"))
        self.label.setText(_translate("ImagePreview", "<html><head/><body><p><span style=\" font-family:\'Verdana,sans-serif\'; font-size:22px;\">⇦</span></p></body></html>"))
        self.label_2.setText(_translate("ImagePreview", "<html><head/><body><p><span style=\" font-family:\'Verdana,sans-serif\'; font-size:22px;\">⇨</span></p></body></html>"))
        self.add_image.setText(_translate("ImagePreview", "Add Image"))

