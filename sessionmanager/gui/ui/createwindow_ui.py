# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createwindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.assets import resource_rc
import qtawesome as fa
from definitions import ROOT_DIR

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
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
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
        qss = open('%s/style.qss' % ROOT_DIR, "r").read()
        home_icon = fa.icon('fa.home', color='grey')
        path_icon = fa.icon('fa.folder-open', color='grey')
        MainWindow.setStyleSheet(qss)
        self.create = QtWidgets.QWidget()
        self.create.setObjectName("create")
        self.info_frame_create = QtWidgets.QFrame(self.create)
        self.info_frame_create.setGeometry(QtCore.QRect(0, 50, 300, 550))
        self.info_frame_create.setMinimumSize(QtCore.QSize(300, 550))
        self.info_frame_create.setStyleSheet("")
        self.info_frame_create.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame_create.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame_create.setObjectName("info_frame_create")
        self.inputs = QtWidgets.QGroupBox(self.info_frame_create)
        self.inputs.setGeometry(QtCore.QRect(10, 10, 281, 471))
        self.inputs.setTitle("")
        self.inputs.setFlat(True)
        self.inputs.setObjectName("inputs")
        self.layoutWidget = QtWidgets.QWidget(self.inputs)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 9, 191, 50))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(80, 50))
        self.label_2.setStyleSheet("border-bottom: 1px dotted grey;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.create_name = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_name.sizePolicy().hasHeightForWidth())
        self.create_name.setSizePolicy(sizePolicy)
        self.create_name.setMaximumSize(QtCore.QSize(189, 24))
        self.create_name.setPlaceholderText("")
        self.create_name.setObjectName("create_name")
        self.verticalLayout.addWidget(self.create_name)
        self.keep_raw = QtWidgets.QCheckBox(self.inputs)
        self.keep_raw.setGeometry(QtCore.QRect(0, 300, 101, 17))
        self.keep_raw.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.keep_raw.setAutoFillBackground(False)
        self.keep_raw.setCheckable(True)
        self.keep_raw.setChecked(False)
        self.keep_raw.setTristate(False)
        self.keep_raw.setObjectName("keep_raw")
        self.error_info = QtWidgets.QLabel(self.inputs)
        self.error_info.setGeometry(QtCore.QRect(0, 350, 281, 131))
        self.error_info.setText("")
        self.error_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.error_info.setWordWrap(True)
        self.error_info.setObjectName("error_info")
        self.create_prog = QtWidgets.QProgressBar(self.inputs)
        self.create_prog.setGeometry(QtCore.QRect(0, 390, 281, 23))
        self.create_prog.setMaximum(0)
        self.create_prog.setProperty("value", 0)
        self.create_prog.setTextVisible(True)
        self.create_prog.setOrientation(QtCore.Qt.Horizontal)
        self.create_prog.setInvertedAppearance(False)
        self.create_prog.setObjectName("create_prog")
        self.layoutWidget1 = QtWidgets.QWidget(self.inputs)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 79, 258, 127))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setMaximumSize(QtCore.QSize(80, 50))
        self.label_8.setStyleSheet("border-bottom: 1px dotted grey;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.create_desc = QtWidgets.QTextEdit(self.layoutWidget1)
        self.create_desc.setMinimumSize(QtCore.QSize(256, 101))
        self.create_desc.setMaximumSize(QtCore.QSize(256, 101))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.create_desc.setFont(font)
        self.create_desc.setObjectName("create_desc")
        self.verticalLayout_2.addWidget(self.create_desc)
        self.layoutWidget2 = QtWidgets.QWidget(self.inputs)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 230, 201, 53))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setMaximumSize(QtCore.QSize(80, 50))
        self.label_5.setStyleSheet("border-bottom: 1px dotted grey;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 0, 0, 1, 1)
        self.path_text = QtWidgets.QLineEdit(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_text.sizePolicy().hasHeightForWidth())
        self.path_text.setSizePolicy(sizePolicy)
        self.path_text.setMaximumSize(QtCore.QSize(189, 24))
        self.path_text.setPlaceholderText("")
        self.path_text.setObjectName("path_text")
        self.gridLayout_8.addWidget(self.path_text, 1, 0, 1, 1)
        self.open_path = QtWidgets.QToolButton(self.layoutWidget2)
        self.open_path.setIcon(path_icon)
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free")
        font.setPointSize(12)
        self.open_path.setFont(font)
        self.open_path.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.open_path.setStyleSheet("")
        self.open_path.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.open_path.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.open_path.setAutoRaise(False)
        self.open_path.setArrowType(QtCore.Qt.NoArrow)
        self.open_path.setObjectName("open_path")
        self.gridLayout_8.addWidget(self.open_path, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.layoutWidget_3 = QtWidgets.QWidget(self.info_frame_create)
        self.layoutWidget_3.setGeometry(QtCore.QRect(170, 501, 121, 42))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setHorizontalSpacing(16)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.create_button = QtWidgets.QPushButton(self.layoutWidget_3)
        self.create_button.setMinimumSize(QtCore.QSize(100, 32))
        self.create_button.setMaximumSize(QtCore.QSize(100, 32))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.create_button.setFont(font)
        self.create_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_button.setDefault(False)
        self.create_button.setFlat(False)
        self.create_button.setObjectName("create_button")
        self.gridLayout_6.addWidget(self.create_button, 0, 0, 1, 1)
        self.navBar_create = QtWidgets.QFrame(self.create)
        self.navBar_create.setGeometry(QtCore.QRect(0, 0, 809, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navBar_create.sizePolicy().hasHeightForWidth())
        self.navBar_create.setSizePolicy(sizePolicy)
        self.navBar_create.setMinimumSize(QtCore.QSize(809, 50))
        self.navBar_create.setMaximumSize(QtCore.QSize(809, 50))
        self.navBar_create.setStyleSheet("")
        self.navBar_create.setObjectName("navBar_create")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.navBar_create)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.home_button = QtWidgets.QPushButton(self.navBar_create)
        self.home_button.setIcon(home_icon)
        self.home_button.setMaximumSize(QtCore.QSize(70, 16777215))
        self.home_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home_button.setFlat(True)
        self.home_button.setObjectName("home_button")
        self.horizontalLayout_4.addWidget(self.home_button)
        self.navSep_create = QtWidgets.QFrame(self.navBar_create)
        self.navSep_create.setStyleSheet("")
        self.navSep_create.setFrameShadow(QtWidgets.QFrame.Plain)
        self.navSep_create.setFrameShape(QtWidgets.QFrame.VLine)
        self.navSep_create.setObjectName("navSep_create")
        self.horizontalLayout_4.addWidget(self.navSep_create)
        self.label_3 = QtWidgets.QLabel(self.navBar_create)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.image_list = QtWidgets.QListWidget(self.create)
        self.image_list.setGeometry(QtCore.QRect(309, 60, 486, 539))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.image_list.setFont(font)
        self.image_list.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.image_list.setMouseTracking(False)
        self.image_list.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.image_list.setAutoFillBackground(False)
        self.image_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.image_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.image_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.image_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.image_list.setProperty("showDropIndicator", False)
        self.image_list.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.image_list.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.image_list.setAlternatingRowColors(False)
        self.image_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.image_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.image_list.setIconSize(QtCore.QSize(60, 60))
        self.image_list.setTextElideMode(QtCore.Qt.ElideNone)
        self.image_list.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.image_list.setMovement(QtWidgets.QListView.Static)
        self.image_list.setFlow(QtWidgets.QListView.LeftToRight)
        self.image_list.setProperty("isWrapping", True)
        self.image_list.setResizeMode(QtWidgets.QListView.Fixed)
        self.image_list.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.image_list.setGridSize(QtCore.QSize(150, 150))
        self.image_list.setViewMode(QtWidgets.QListView.IconMode)
        self.image_list.setModelColumn(0)
        self.image_list.setUniformItemSizes(False)
        self.image_list.setBatchSize(100)
        self.image_list.setWordWrap(False)
        self.image_list.setSelectionRectVisible(False)
        self.image_list.setObjectName("image_list")
        MainWindow.addWidget(self.create)

        self.retranslateUi(MainWindow)
        MainWindow.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Session Manager"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.keep_raw.setToolTip(_translate("MainWindow", "Store RAW files for extraction if needed"))
        self.keep_raw.setText(_translate("MainWindow", "Keep Raw"))
        self.create_prog.setFormat(_translate("MainWindow", "%p%"))
        self.label_8.setText(_translate("MainWindow", "Description"))
        self.create_desc.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Path"))
        self.open_path.setText(_translate("MainWindow", "folder-open"))
        self.create_button.setText(_translate("MainWindow", "Create"))
        self.navBar_create.setAccessibleName(_translate("MainWindow", "navBar"))
        self.home_button.setText(_translate("MainWindow", "Home"))
        self.label_3.setText(_translate("MainWindow", "Create A New Session"))
        self.image_list.setSortingEnabled(False)

