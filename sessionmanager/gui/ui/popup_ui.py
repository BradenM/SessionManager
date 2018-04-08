# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_popup(object):
    def setupUi(self, popup):
        popup.setObjectName("popup")
        popup.setWindowModality(QtCore.Qt.ApplicationModal)
        popup.resize(400, 200)
        popup.setMinimumSize(QtCore.QSize(400, 200))
        popup.setMaximumSize(QtCore.QSize(400, 200))
        popup.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(popup)
        self.buttonBox.setGeometry(QtCore.QRect(30, 150, 341, 40))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(popup)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 10, 341, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.info = QtWidgets.QLabel(self.gridLayoutWidget)
        self.info.setStyleSheet(" font-size:18pt; font-weight:600; color:#ff0000;")
        self.info.setLineWidth(2)
        self.info.setObjectName("info")
        self.gridLayout.addWidget(self.info, 0, 0, 1, 1)
        self.desc = QtWidgets.QLabel(self.gridLayoutWidget)
        self.desc.setWordWrap(True)
        self.desc.setObjectName("desc")
        self.gridLayout.addWidget(self.desc, 0, 1, 1, 1)

        self.retranslateUi(popup)
        self.buttonBox.accepted.connect(popup.accept)
        self.buttonBox.rejected.connect(popup.reject)
        QtCore.QMetaObject.connectSlotsByName(popup)

    def retranslateUi(self, popup):
        _translate = QtCore.QCoreApplication.translate
        popup.setWindowTitle(_translate("popup", "popup_title"))
        self.info.setText(_translate("popup", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">WARNING:</span></p></body></html>"))
        self.desc.setText(_translate("popup", "session infos"))

