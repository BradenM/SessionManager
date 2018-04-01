# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeletePopup(object):
    def setupUi(self, DeletePopup):
        DeletePopup.setObjectName("DeletePopup")
        DeletePopup.setWindowModality(QtCore.Qt.ApplicationModal)
        DeletePopup.resize(400, 200)
        DeletePopup.setMinimumSize(QtCore.QSize(400, 200))
        DeletePopup.setMaximumSize(QtCore.QSize(400, 200))
        DeletePopup.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(DeletePopup)
        self.buttonBox.setGeometry(QtCore.QRect(30, 150, 341, 40))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(DeletePopup)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 10, 341, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.deleteInfo = QtWidgets.QLabel(self.gridLayoutWidget)
        self.deleteInfo.setWordWrap(True)
        self.deleteInfo.setObjectName("deleteInfo")
        self.gridLayout.addWidget(self.deleteInfo, 0, 1, 1, 1)

        self.retranslateUi(DeletePopup)
        self.buttonBox.accepted.connect(DeletePopup.accept)
        self.buttonBox.rejected.connect(DeletePopup.reject)
        QtCore.QMetaObject.connectSlotsByName(DeletePopup)

    def retranslateUi(self, DeletePopup):
        _translate = QtCore.QCoreApplication.translate
        DeletePopup.setWindowTitle(_translate("DeletePopup", "Delete Session"))
        self.label.setText(_translate("DeletePopup", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">WARNING:</span></p></body></html>"))
        self.deleteInfo.setText(_translate("DeletePopup", "session info"))

