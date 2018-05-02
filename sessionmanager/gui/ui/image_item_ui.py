# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_item_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImageItem(object):
    def setupUi(self, ImageItem):
        ImageItem.setObjectName("ImageItem")
        ImageItem.resize(200, 150)
        ImageItem.setMinimumSize(QtCore.QSize(200, 150))
        ImageItem.setMaximumSize(QtCore.QSize(200, 150))
        ImageItem.setStyleSheet("padding:0px;\n"
"margin:0px;")
        self.image_widget = QtWidgets.QWidget(ImageItem)
        self.image_widget.setGeometry(QtCore.QRect(0, 0, 200, 150))
        self.image_widget.setMinimumSize(QtCore.QSize(200, 150))
        self.image_widget.setMaximumSize(QtCore.QSize(200, 150))
        self.image_widget.setObjectName("image_widget")
        self.image = QtWidgets.QLabel(self.image_widget)
        self.image.setGeometry(QtCore.QRect(0, 0, 200, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setMinimumSize(QtCore.QSize(200, 150))
        self.image.setMaximumSize(QtCore.QSize(200, 150))
        self.image.setBaseSize(QtCore.QSize(200, 0))
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.overlay = QtWidgets.QWidget(ImageItem)
        self.overlay.setGeometry(QtCore.QRect(0, 0, 200, 150))
        self.overlay.setMinimumSize(QtCore.QSize(200, 150))
        self.overlay.setMaximumSize(QtCore.QSize(200, 150))
        self.overlay.setStyleSheet("background-color:rgba(27,27,27,0.7);\n"
"")
        self.overlay.setObjectName("overlay")
        self.overlay_icon = QtWidgets.QLabel(self.overlay)
        self.overlay_icon.setGeometry(QtCore.QRect(0, 0, 200, 150))
        self.overlay_icon.setStyleSheet("background-color:none;")
        self.overlay_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.overlay_icon.setObjectName("overlay_icon")

        self.retranslateUi(ImageItem)
        QtCore.QMetaObject.connectSlotsByName(ImageItem)

    def retranslateUi(self, ImageItem):
        _translate = QtCore.QCoreApplication.translate
        ImageItem.setWindowTitle(_translate("ImageItem", "Form"))
        self.image.setText(_translate("ImageItem", "image"))
        self.overlay_icon.setText(_translate("ImageItem", "logo"))

