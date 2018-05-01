# Program: Session Manager
# File: gui/widgets/image_preview.py
# Desc: Image Preview Overlay
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.image_preview_ui import Ui_ImagePreview
from gui import gui_handle as handle
import os


class ImagePreviewOverlay(QtWidgets.QWidget):
    def __init__(self, parent, session):
        super(ImagePreviewOverlay, self).__init__(parent)
        self.ui = Ui_ImagePreview()
        self.ui.setupUi(self)

        # Vars
        self.parent = parent
        self.session = session
        self.raw_thumbs = handle.get_thumbs(self.session, "RAW")

        # Connections
        self.ui.close_overlay.clicked.connect(self.close)
        self.ui.slider.itemClicked.connect(self.set_image)
        self.ui.add_image.clicked.connect(self.add_image)

        # Setup
        self.slider()

    def active(self, thumb=False):
        image = self.ui.slider.currentItem().data
        if thumb:
            return image(QtCore.Qt.UserRole)
        else:
            p = image(QtCore.Qt.AccessibleDescriptionRole)
            return os.path.basename(p)

    def set_image(self):
        self.ui.add_image.setEnabled(True)
        image = self.active("thumb")
        name = self.active()
        self.ui.file_name.setText(name)
        self.ui.preview_image.setPixmap(QtGui.QPixmap(image).scaled(500, 500, QtCore.Qt.KeepAspectRatio))

    def add_image(self):
        image = self.ui.slider.currentItem().data(QtCore.Qt.AccessibleDescriptionRole)
        print(image)
        handle.update_pos(self.session, image, "PHOTO")
        self.slider()

    def slider(self):
        self.ui.slider.setIconSize(QtCore.QSize(128, 128))
        for img, thumb in self.raw_thumbs.items():
            item = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon(thumb)
            item.setIcon(icon)
            item.setData(QtCore.Qt.AccessibleDescriptionRole, img)
            item.setData(QtCore.Qt.UserRole, thumb)
            self.ui.slider.addItem(item)

    def close(self):
        self.parent.close_overlay(self)