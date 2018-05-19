# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usbwindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from definitions import ICONS

class Ui_USBWindow(object):
    def setupUi(self, USBWindow):
        USBWindow.setObjectName("USBWindow")
        USBWindow.resize(500, 250)
        USBWindow.setMaximumSize(QtCore.QSize(500, 250))
        USBWindow.setAutoFillBackground(True)
        USBWindow.setStyleSheet("QFrame{\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QLabel[title=true]{\n"
"    font: 28px \"Montserrat\";\n"
"    color:#f2f2f2;\n"
"    font-weight:900;\n"
"}\n"
"\n"
"QLabel{\n"
"    font:16px \"Lato\";\n"
"    color:#f2f2f2;\n"
"    font-weight:300;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color:white;\n"
"    background-color:#1473e6;\n"
"    border-style:solid;\n"
"    border-width:2px;\n"
"    border-radius:14px;\n"
"    border-color:#1473e6;\n"
"    padding:6 18 6 18px;\n"
"    font:16pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:white;\n"
"    background-color:#2b81e8;\n"
"    border-style:solid;\n"
"    border-width:2px;\n"
"    border-radius:14px;\n"
"    border-color:#2b81e8;\n"
"    padding:6 18 6 18px;\n"
"    font:16pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton[no=true]:hover{\n"
"    color:white;\n"
"    border-color:white;\n"
"    background-color:rgba(211,211,211, 0.1);\n"
"}\n"
"\n"
"QPushButton[no=true]{\n"
"    color:#D3D3D3;\n"
"    background-color:rgba(0,0,0,0);\n"
"    border-style:solid;\n"
"    border-width:2px;\n"
"    border-radius:14px;\n"
"    border-color:#D3D3D3;\n"
"    padding:6 18 6 18px;\n"
"    font:16pt \"Roboto\";\n"
"}")
        self.main_frame = QtWidgets.QFrame(USBWindow)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 500, 250))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.label = QtWidgets.QLabel(self.main_frame)
        self.label.setGeometry(QtCore.QRect(40, 60, 141, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(f"{ICONS}/usb.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.main_frame)
        self.label_2.setGeometry(QtCore.QRect(0, 3, 500, 50))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setProperty("title", True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.main_frame)
        self.label_3.setGeometry(QtCore.QRect(240, 86, 201, 71))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(self.main_frame)
        self.widget.setGeometry(QtCore.QRect(260, 200, 216, 42))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(14)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create = QtWidgets.QPushButton(self.widget)
        self.create.setMinimumSize(QtCore.QSize(100, 40))
        self.create.setMaximumSize(QtCore.QSize(100, 40))
        self.create.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create.setProperty("yes", False)
        self.create.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.create)
        self.close = QtWidgets.QPushButton(self.widget)
        self.close.setMinimumSize(QtCore.QSize(100, 40))
        self.close.setMaximumSize(QtCore.QSize(100, 40))
        self.close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close.setProperty("no", True)
        self.close.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.close)

        self.retranslateUi(USBWindow)
        QtCore.QMetaObject.connectSlotsByName(USBWindow)

    def retranslateUi(self, USBWindow):
        _translate = QtCore.QCoreApplication.translate
        USBWindow.setWindowTitle(_translate("USBWindow", "Form"))
        self.label_2.setText(_translate("USBWindow", "Session Manager"))
        self.label_3.setText(_translate("USBWindow", "A USB with RAW images has been inserted. Would you like to create a session?"))
        self.create.setText(_translate("USBWindow", "Create"))
        self.close.setText(_translate("USBWindow", "No"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    USBWindow = QtWidgets.QWidget()
    ui = Ui_USBWindow()
    ui.setupUi(USBWindow)
    USBWindow.show()
    sys.exit(app.exec_())

