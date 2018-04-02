# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Manage(object):
    def setupUi(self, Manage):
        Manage.setObjectName("Manage")
        Manage.resize(800, 700)
        Manage.setMinimumSize(QtCore.QSize(800, 700))
        Manage.setMaximumSize(QtCore.QSize(800, 700))
        self.raw = QtWidgets.QWidget()
        self.raw.setObjectName("raw")
        self.groupBox = QtWidgets.QGroupBox(self.raw)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 771, 361))
        self.groupBox.setObjectName("groupBox")
        self.image = QtWidgets.QLabel(self.groupBox)
        self.image.setGeometry(QtCore.QRect(10, 20, 751, 331))
        self.image.setObjectName("image")
        self.imageSlider = QtWidgets.QListView(self.raw)
        self.imageSlider.setGeometry(QtCore.QRect(10, 380, 771, 141))
        self.imageSlider.setObjectName("imageSlider")
        Manage.addTab(self.raw, "")

        self.retranslateUi(Manage)
        QtCore.QMetaObject.connectSlotsByName(Manage)

    def retranslateUi(self, Manage):
        _translate = QtCore.QCoreApplication.translate
        Manage.setWindowTitle(_translate("Manage", "Manage"))
        self.groupBox.setTitle(_translate("Manage", "Preview"))
        self.image.setText(_translate("Manage", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#505050;\">Select an image to preview</span></p></body></html>"))
        Manage.setTabText(Manage.indexOf(self.raw), _translate("Manage", "RAW"))

