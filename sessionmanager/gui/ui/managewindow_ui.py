# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'managewindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Manage(object):
    def setupUi(self, Manage):
        Manage.setObjectName("Manage")
        Manage.resize(800, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Manage.sizePolicy().hasHeightForWidth())
        Manage.setSizePolicy(sizePolicy)
        Manage.setStyleSheet("QListView\n"
"{\n"
"outline: none;\n"
"}\n"
"QListWidget\n"
"{\n"
"outline: none;\n"
"}\n"
"@QListView\n"
"{\n"
"outline: none;\n"
"}@\n"
"@QListWidget\n"
"{\n"
"outline: none;\n"
"}@")
        self.verticalFrame = QtWidgets.QFrame(Manage)
        self.verticalFrame.setGeometry(QtCore.QRect(0, 0, 800, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setMinimumSize(QtCore.QSize(800, 700))
        self.verticalFrame.setMaximumSize(QtCore.QSize(800, 700))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalFrame)
        self.tabWidget.setStyleSheet("QListWidget:focus{\n"
"border:none;\n"
"}\n"
"QListWidget:selected{\n"
"border:none;\n"
"}\n"
"QListWidget{\n"
"outline:none;\n"
"}\n"
"@QListWidget\n"
"{\n"
"outline: none;\n"
"}@\n"
"@QListView\n"
"{\n"
"outline: none;\n"
"}@")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_raw = QtWidgets.QWidget()
        self.tab_raw.setStyleSheet("QListWidget:focus{\n"
"border:none;\n"
"}\n"
"QListWidget:focus{\n"
"border:none;\n"
"}\n"
"@QListView\n"
"{\n"
"outline: none;\n"
"}@")
        self.tab_raw.setObjectName("tab_raw")
        self.groupBox = QtWidgets.QGroupBox(self.tab_raw)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 771, 380))
        self.groupBox.setStyleSheet("color:rgb(80, 80, 80)")
        self.groupBox.setObjectName("groupBox")
        self.preview_label = QtWidgets.QLabel(self.groupBox)
        self.preview_label.setEnabled(True)
        self.preview_label.setGeometry(QtCore.QRect(10, 20, 751, 351))
        self.preview_label.setStyleSheet(" font-size:16pt; color:#505050;")
        self.preview_label.setObjectName("preview_label")
        self.thumb_slider = QtWidgets.QListWidget(self.tab_raw)
        self.thumb_slider.setGeometry(QtCore.QRect(2, 410, 760, 140))
        self.thumb_slider.setMinimumSize(QtCore.QSize(760, 140))
        self.thumb_slider.setMaximumSize(QtCore.QSize(760, 140))
        self.thumb_slider.setStyleSheet("padding-top:5px; font-size:12pt; \n"
"color:#505050;")
        self.thumb_slider.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.thumb_slider.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.thumb_slider.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.thumb_slider.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.thumb_slider.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.thumb_slider.setIconSize(QtCore.QSize(125, 125))
        self.thumb_slider.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.thumb_slider.setMovement(QtWidgets.QListView.Free)
        self.thumb_slider.setFlow(QtWidgets.QListView.LeftToRight)
        self.thumb_slider.setProperty("isWrapping", False)
        self.thumb_slider.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.thumb_slider.setGridSize(QtCore.QSize(150, 130))
        self.thumb_slider.setViewMode(QtWidgets.QListView.IconMode)
        self.thumb_slider.setUniformItemSizes(False)
        self.thumb_slider.setSelectionRectVisible(True)
        self.thumb_slider.setObjectName("thumb_slider")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_raw)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(470, 580, 271, 60))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.proof_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proof_button.sizePolicy().hasHeightForWidth())
        self.proof_button.setSizePolicy(sizePolicy)
        self.proof_button.setObjectName("proof_button")
        self.gridLayout_2.addWidget(self.proof_button, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.rename_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.rename_text.setObjectName("rename_text")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rename_text)
        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_raw)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-10, 570, 320, 70))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.preview_loader = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.preview_loader.setObjectName("preview_loader")
        self.horizontalLayout.addWidget(self.preview_loader, 0, QtCore.Qt.AlignRight)
        self.preview_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_text.sizePolicy().hasHeightForWidth())
        self.preview_text.setSizePolicy(sizePolicy)
        self.preview_text.setMinimumSize(QtCore.QSize(0, 0))
        self.preview_text.setMaximumSize(QtCore.QSize(371, 329))
        self.preview_text.setObjectName("preview_text")
        self.horizontalLayout.addWidget(self.preview_text)
        self.tabWidget.addTab(self.tab_raw, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("@QListWidget\n"
"{\n"
"outline: none;\n"
"}@")
        self.tab_2.setObjectName("tab_2")
        self.proof_thumbs = QtWidgets.QListWidget(self.tab_2)
        self.proof_thumbs.setGeometry(QtCore.QRect(10, 20, 760, 431))
        self.proof_thumbs.setAutoFillBackground(True)
        self.proof_thumbs.setStyleSheet("padding-top:10px;\n"
"background-color:#f2f2f2;\n"
"border:none;\n"
"outline:none;\n"
"QListView{\n"
"outline:none;\n"
"}\n"
"")
        self.proof_thumbs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.proof_thumbs.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.proof_thumbs.setLineWidth(1)
        self.proof_thumbs.setMidLineWidth(0)
        self.proof_thumbs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.proof_thumbs.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.proof_thumbs.setProperty("showDropIndicator", False)
        self.proof_thumbs.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.proof_thumbs.setIconSize(QtCore.QSize(180, 180))
        self.proof_thumbs.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.proof_thumbs.setMovement(QtWidgets.QListView.Free)
        self.proof_thumbs.setFlow(QtWidgets.QListView.LeftToRight)
        self.proof_thumbs.setProperty("isWrapping", True)
        self.proof_thumbs.setResizeMode(QtWidgets.QListView.Fixed)
        self.proof_thumbs.setGridSize(QtCore.QSize(240, 200))
        self.proof_thumbs.setViewMode(QtWidgets.QListView.IconMode)
        self.proof_thumbs.setSelectionRectVisible(False)
        self.proof_thumbs.setObjectName("proof_thumbs")
        self.open_proof = QtWidgets.QPushButton(self.tab_2)
        self.open_proof.setGeometry(QtCore.QRect(630, 580, 101, 23))
        self.open_proof.setObjectName("open_proof")
        self.proofInfo = QtWidgets.QGroupBox(self.tab_2)
        self.proofInfo.setGeometry(QtCore.QRect(10, 470, 381, 170))
        self.proofInfo.setStyleSheet("color:rgb(80, 80, 80)")
        self.proofInfo.setObjectName("proofInfo")
        self.formLayoutWidget = QtWidgets.QWidget(self.proofInfo)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 30, 240, 127))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.name_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name_edit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.name_edit.setObjectName("name_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_edit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.file_name = QtWidgets.QLabel(self.formLayoutWidget)
        self.file_name.setObjectName("file_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.file_name)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.file_date = QtWidgets.QLabel(self.formLayoutWidget)
        self.file_date.setText("")
        self.file_date.setObjectName("file_date")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.file_date)
        self.update_proof = QtWidgets.QPushButton(self.formLayoutWidget)
        self.update_proof.setMaximumSize(QtCore.QSize(91, 23))
        self.update_proof.setStyleSheet("color:rgb(0, 0, 0)")
        self.update_proof.setObjectName("update_proof")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.update_proof)
        self.finalize_proof = QtWidgets.QPushButton(self.tab_2)
        self.finalize_proof.setGeometry(QtCore.QRect(630, 610, 101, 23))
        self.finalize_proof.setObjectName("finalize_proof")
        self.tabWidget.addTab(self.tab_2, "")
        self.finals_tab = QtWidgets.QWidget()
        self.finals_tab.setObjectName("finals_tab")
        self.final_thumbs = QtWidgets.QListWidget(self.finals_tab)
        self.final_thumbs.setGeometry(QtCore.QRect(10, 20, 760, 431))
        self.final_thumbs.setAutoFillBackground(True)
        self.final_thumbs.setStyleSheet("padding-top:10px;\n"
"background-color:#f2f2f2;\n"
"border:none;\n"
"outline:none;\n"
"QListView{\n"
"outline:none;\n"
"}\n"
"")
        self.final_thumbs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.final_thumbs.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.final_thumbs.setLineWidth(1)
        self.final_thumbs.setMidLineWidth(0)
        self.final_thumbs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.final_thumbs.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.final_thumbs.setProperty("showDropIndicator", False)
        self.final_thumbs.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.final_thumbs.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.final_thumbs.setIconSize(QtCore.QSize(180, 180))
        self.final_thumbs.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.final_thumbs.setMovement(QtWidgets.QListView.Free)
        self.final_thumbs.setFlow(QtWidgets.QListView.LeftToRight)
        self.final_thumbs.setProperty("isWrapping", True)
        self.final_thumbs.setResizeMode(QtWidgets.QListView.Fixed)
        self.final_thumbs.setGridSize(QtCore.QSize(240, 200))
        self.final_thumbs.setViewMode(QtWidgets.QListView.IconMode)
        self.final_thumbs.setSelectionRectVisible(False)
        self.final_thumbs.setObjectName("final_thumbs")
        self.export_button = QtWidgets.QPushButton(self.finals_tab)
        self.export_button.setGeometry(QtCore.QRect(610, 460, 90, 23))
        self.export_button.setObjectName("export_button")
        self.tabWidget.addTab(self.finals_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Manage)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Manage)

    def retranslateUi(self, Manage):
        _translate = QtCore.QCoreApplication.translate
        Manage.setWindowTitle(_translate("Manage", "SessionManager - Manage"))
        self.groupBox.setTitle(_translate("Manage", "Preview"))
        self.preview_label.setText(_translate("Manage", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#505050;\">Select an image to preview</span></p></body></html>"))
        self.thumb_slider.setSortingEnabled(False)
        self.proof_button.setText(_translate("Manage", "Make Proof"))
        self.label.setText(_translate("Manage", "<html><head/><body><p><span style=\" font-size:12pt; color:#505050;\">Rename:</span></p></body></html>"))
        self.preview_loader.setText(_translate("Manage", "<html><head/><body><p>asdasd</p></body></html>"))
        self.preview_text.setText(_translate("Manage", "<html><head/><body><p><span style=\" font-size:16pt; color:#505050;\">Generating Thumbnails...</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_raw), _translate("Manage", "RAW"))
        self.open_proof.setText(_translate("Manage", "Open"))
        self.proofInfo.setTitle(_translate("Manage", "Proof Info"))
        self.label_2.setText(_translate("Manage", "<html><head/><body><p><span style=\" font-size:12pt;\">Name:</span></p></body></html>"))
        self.label_3.setText(_translate("Manage", "<html><head/><body><p><span style=\" font-size:12pt; color:#505050;\">File Name:</span></p></body></html>"))
        self.file_name.setText(_translate("Manage", "<html><head/><body><p><span style=\" font-size:12pt;\">examplefile.dng</span></p></body></html>"))
        self.label_5.setText(_translate("Manage", "<html><head/><body><p><span style=\" font-size:12pt;\">Last Opened: </span></p></body></html>"))
        self.update_proof.setText(_translate("Manage", "Update"))
        self.finalize_proof.setText(_translate("Manage", "Finalize"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Manage", "Proofs"))
        self.export_button.setText(_translate("Manage", "Export"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.finals_tab), _translate("Manage", "Finals"))

