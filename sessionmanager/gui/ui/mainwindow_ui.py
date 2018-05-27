# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.assets import resource_rc
import qtawesome as fa
from definitions import STYLE


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 700))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setFrameShape(QtWidgets.QFrame.NoFrame)
        QtGui.QFontDatabase.addApplicationFont("gui/ui/assets/fonts/fa-regular-400.ttf")
        QtGui.QFontDatabase.addApplicationFont("gui/ui/assets/fonts/Montserrat-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont("gui/ui/assets/fonts/Lato-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont("gui/ui/assets/fonts/Roboto-Light.ttf")
        QtGui.QFontDatabase.addApplicationFont("gui/ui/assets/fonts/Roboto-Medium.ttf")
        search_icon = fa.icon('fa.search', color='grey')
        recent_icon = fa.icon('fa.clock-o', color='grey')
        settings_icon = fa.icon('fa.cog', color='grey')
        MainWindow.setStyleSheet(STYLE)
        self.home = QtWidgets.QWidget()
        self.home.setStyleSheet("")
        self.home.setObjectName("home")
        self.navBar = QtWidgets.QFrame(self.home)
        self.navBar.setGeometry(QtCore.QRect(0, 0, 809, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navBar.sizePolicy().hasHeightForWidth())
        self.navBar.setSizePolicy(sizePolicy)
        self.navBar.setMinimumSize(QtCore.QSize(0, 50))
        self.navBar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.navBar.setStyleSheet("")
        self.navBar.setObjectName("navBar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.navBar)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.recent_button = QtWidgets.QPushButton(self.navBar)
        self.recent_button.setIcon(recent_icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recent_button.sizePolicy().hasHeightForWidth())
        self.recent_button.setSizePolicy(sizePolicy)
        self.recent_button.setMinimumSize(QtCore.QSize(70, 0))
        self.recent_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.recent_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recent_button.setFlat(True)
        self.recent_button.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.recent_button, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.search_bar = QtWidgets.QFormLayout()
        self.search_bar.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.search_bar.setObjectName("search_bar")
        self.session_filter = QtWidgets.QLineEdit(self.navBar)
        self.session_filter.setMaximumSize(QtCore.QSize(133, 20))
        self.session_filter.setFrame(False)
        self.session_filter.setObjectName("session_filter")
        self.search_bar.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.session_filter)
        self.search_ico = QtWidgets.QPushButton(self.navBar)
        self.search_ico.setIcon(search_icon)
        self.search_ico.setMaximumSize(QtCore.QSize(24, 24))
        self.search_ico.setText("")
        self.search_ico.setFlat(True)
        self.search_ico.setObjectName("search_ico")
        self.search_bar.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.search_ico)
        self.gridLayout.addLayout(self.search_bar, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.navSep = QtWidgets.QFrame(self.navBar)
        self.navSep.setStyleSheet("")
        self.navSep.setFrameShadow(QtWidgets.QFrame.Plain)
        self.navSep.setFrameShape(QtWidgets.QFrame.VLine)
        self.navSep.setObjectName("navSep")
        self.horizontalLayout.addWidget(self.navSep)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.open_settings = QtWidgets.QPushButton(self.navBar)
        self.open_settings.setIcon(settings_icon)
        self.open_settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.open_settings.setFlat(True)
        self.open_settings.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.open_settings, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 1)
        self.create_tab = QtWidgets.QPushButton(self.navBar)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.create_tab.setFont(font)
        self.create_tab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_tab.setFlat(True)
        self.create_tab.setObjectName("create_tab")
        self.gridLayout_2.addWidget(self.create_tab, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(175, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.sessionlist_header = QtWidgets.QFrame(self.home)
        self.sessionlist_header.setGeometry(QtCore.QRect(20, 60, 191, 43))
        self.sessionlist_header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sessionlist_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sessionlist_header.setObjectName("sessionlist_header")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.sessionlist_header)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.sessionlist_header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.sessionlist_count = QtWidgets.QLabel(self.sessionlist_header)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sessionlist_count.setFont(font)
        self.sessionlist_count.setAlignment(QtCore.Qt.AlignCenter)
        self.sessionlist_count.setObjectName("sessionlist_count")
        self.gridLayout_4.addWidget(self.sessionlist_count, 0, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_4)
        self.info_frame = QtWidgets.QFrame(self.home)
        self.info_frame.setGeometry(QtCore.QRect(500, 50, 300, 550))
        self.info_frame.setStyleSheet("")
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")
        self.details = QtWidgets.QGroupBox(self.info_frame)
        self.details.setGeometry(QtCore.QRect(10, 10, 296, 471))
        self.details.setFlat(False)
        self.details.setObjectName("details")
        self.session_name = QtWidgets.QLabel(self.details)
        self.session_name.setGeometry(QtCore.QRect(-3, 9, 291, 73))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.session_name.sizePolicy().hasHeightForWidth())
        self.session_name.setSizePolicy(sizePolicy)
        self.session_name.setMinimumSize(QtCore.QSize(123, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.session_name.setFont(font)
        self.session_name.setWordWrap(True)
        self.session_name.setObjectName("session_name")
        self.groupBox_2 = QtWidgets.QGroupBox(self.details)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 88, 276, 203))
        self.groupBox_2.setMinimumSize(QtCore.QSize(276, 203))
        self.groupBox_2.setMaximumSize(QtCore.QSize(276, 203))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.desc_box = QtWidgets.QTextBrowser(self.groupBox_2)
        self.desc_box.setGeometry(QtCore.QRect(-3, 23, 256, 101))
        self.desc_box.setMaximumSize(QtCore.QSize(256, 101))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.desc_box.setFont(font)
        self.desc_box.setObjectName("desc_box")
        self.info_misc = QtWidgets.QGroupBox(self.details)
        self.info_misc.setGeometry(QtCore.QRect(0, 252, 268, 191))
        self.info_misc.setMinimumSize(QtCore.QSize(191, 111))
        self.info_misc.setFlat(False)
        self.info_misc.setObjectName("info_misc")
        self.layoutWidget = QtWidgets.QWidget(self.info_misc)
        self.layoutWidget.setGeometry(QtCore.QRect(2, 30, 290, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self._2 = QtWidgets.QFormLayout(self.layoutWidget)
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setObjectName("_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self._2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.image_count = QtWidgets.QLabel(self.layoutWidget)
        self.image_count.setText("")
        self.image_count.setAlignment(QtCore.Qt.AlignCenter)
        self.image_count.setObjectName("image_count")
        self._2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.image_count)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self._2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.create_date = QtWidgets.QLabel(self.layoutWidget)
        self.create_date.setText("")
        self.create_date.setAlignment(QtCore.Qt.AlignCenter)
        self.create_date.setObjectName("create_date")
        self._2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.create_date)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self._2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.has_raw = QtWidgets.QLabel(self.layoutWidget)
        self.has_raw.setText("")
        self.has_raw.setAlignment(QtCore.Qt.AlignCenter)
        self.has_raw.setObjectName("has_raw")
        self._2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.has_raw)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self._2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.modify_date = QtWidgets.QLabel(self.layoutWidget)
        self.modify_date.setText("")
        self.modify_date.setAlignment(QtCore.Qt.AlignCenter)
        self.modify_date.setObjectName("modify_date")
        self._2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.modify_date)
        self.layoutWidget1 = QtWidgets.QWidget(self.info_frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(90, 501, 195, 42))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setHorizontalSpacing(16)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.open_button = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.open_button.setFont(font)
        self.open_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.open_button.setDefault(False)
        self.open_button.setFlat(False)
        self.open_button.setObjectName("open_button")
        self.gridLayout_5.addWidget(self.open_button, 0, 0, 1, 1)
        self.close_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.close_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_button.setFlat(False)
        self.close_button.setObjectName("close_button")
        self.gridLayout_5.addWidget(self.close_button, 0, 1, 1, 1)
        self.sessionList = QtWidgets.QListWidget(self.home)
        self.sessionList.setGeometry(QtCore.QRect(9, 105, 476, 480))
        self.sessionList.setMinimumSize(QtCore.QSize(476, 480))
        self.sessionList.setMaximumSize(QtCore.QSize(476, 480))
        self.sessionList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sessionList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sessionList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.sessionList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.sessionList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.sessionList.setTextElideMode(QtCore.Qt.ElideNone)
        self.sessionList.setMovement(QtWidgets.QListView.Static)
        self.sessionList.setFlow(QtWidgets.QListView.LeftToRight)
        self.sessionList.setProperty("isWrapping", True)
        self.sessionList.setResizeMode(QtWidgets.QListView.Adjust)
        self.sessionList.setGridSize(QtCore.QSize(200, 200))
        self.sessionList.setViewMode(QtWidgets.QListView.IconMode)
        self.sessionList.setUniformItemSizes(False)
        self.sessionList.setSelectionRectVisible(False)
        self.sessionList.setObjectName("sessionList")
        self.session_hint = QtWidgets.QLabel(self.home)
        self.session_hint.setGeometry(QtCore.QRect(10, 60, 471, 480))
        self.session_hint.setStyleSheet("color:#696969;\n"
"font:20pt \"Lato\";\n"
"font-weight:900;")
        self.session_hint.setObjectName("session_hint")
        MainWindow.addWidget(self.home)

        self.retranslateUi(MainWindow)
        MainWindow.setCurrentIndex(0)
        self.close_button.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Session Manager"))
        self.navBar.setAccessibleName(_translate("MainWindow", "navBar"))
        self.recent_button.setText(_translate("MainWindow", "Recent"))
        self.session_filter.setPlaceholderText(_translate("MainWindow", "Search"))
        self.open_settings.setText(_translate("MainWindow", "Settings"))
        self.create_tab.setText(_translate("MainWindow", "Create"))
        self.label.setText(_translate("MainWindow", "YOUR SESSIONS"))
        self.sessionlist_count.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(1)</p></body></html>"))
        self.details.setTitle(_translate("MainWindow", "SESSION DETAILS"))
        self.session_name.setText(_translate("MainWindow", "<html><head/><body><p>Goudie Family</p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Description"))
        self.desc_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Example Description</p></body></html>"))
        self.info_misc.setTitle(_translate("MainWindow", "Information"))
        self.label_4.setText(_translate("MainWindow", "Images:"))
        self.label_6.setText(_translate("MainWindow", "Creation Date:"))
        self.label_9.setText(_translate("MainWindow", "Raw Saved:"))
        self.label_11.setText(_translate("MainWindow", "Last Modified:"))
        self.open_button.setText(_translate("MainWindow", "Open"))
        self.close_button.setText(_translate("MainWindow", "Close"))
        self.session_hint.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Click create or plug in your camera</p><p align=\"center\">memory card to create your first Session</p></body></html>"))

