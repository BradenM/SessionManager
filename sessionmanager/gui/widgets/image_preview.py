# Program: Session Manager
# File: gui/widgets/image_preview.py
# Desc: Image Preview Overlay
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.image_preview_ui import Ui_ImagePreview
from gui import gui_handle as handle


class ImagePreviewOverlay(QtWidgets.QWidget):
    def __init__(self, parent, session):
        super(ImagePreviewOverlay, self).__init__(parent)
        self.ui = Ui_ImagePreview()
        self.ui.setupUi(self)

        # Vars
        self.parent = parent
        self.session = session
        self.hint = self.ui.preview_image.text()

        # Connections
        self.ui.close_overlay.clicked.connect(self.close)
        self.ui.slider.itemClicked.connect(self.set_image)
        self.ui.add_image.clicked.connect(self.add_image)

        # Setup
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(8)
        #self.setGraphicsEffect(shadow)
        self.slider()

    def active(self):
        active = self.ui.slider.currentItem().data(QtCore.Qt.UserRole)
        return active

    def set_image(self):
        self.ui.add_image.setEnabled(True)
        img = self.active()
        self.ui.file_name.setText(img.name)
        self.ui.preview_image.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.preview_image.setPixmap(QtGui.QPixmap(img.thumb).scaled(600, 600, QtCore.Qt.KeepAspectRatio))

    def add_image(self):
        img = self.active()
        handle.update_pos(img, "PHOTO")
        self.ui.slider.clear()
        self.ui.preview_image.setText(self.hint)
        self.slider()

    def slider(self):
        self.ui.slider.clear()
        self.ui.slider.setIconSize(QtCore.QSize(128, 128))
        images = handle.get_images(self.session, "RAW")
        for img in images:
            item = QtWidgets.QListWidgetItem(self.ui.slider)
            icon = QtGui.QIcon(img.thumb)
            item.setIcon(icon)
            item.setData(QtCore.Qt.UserRole, img)
            self.ui.slider.addItem(item)

    def close(self):
        self.parent.close_overlay(self)