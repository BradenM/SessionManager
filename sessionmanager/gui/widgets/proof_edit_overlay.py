# Program: Session Manager
# File: gui/widgets/proof_edit_overlay.py
# Desc: Overlay for editing proofs
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.logo_crop_overlay_ui import Ui_EditOverlay
from gui import gui_handle as handle


class EditOverlay(QtWidgets.QWidget):
    def __init__(self, parent, img):
        super(EditOverlay, self).__init__()
        self.ui = Ui_EditOverlay()
        self.ui.setupUi(self)

        # Vars
        self.parent = parent
        self.image = img
        self.scene = QtWidgets.QGraphicsScene(self)

        # Connections

        # Setup
        self.load_image()

    # Functions
    def load_image(self):
        img = QtWidgets.QGraphicsPixmapItem(self.image.jpg)
        self.scene.addItem(img)
        self.ui.edit_view.setScene(self.scene)
