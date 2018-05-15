# Program: Session Manager
# File: gui/widgets/proof_overlay.py
# Desc: Finals overlay for proofs
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.proofoverlay_ui import Ui_MainOverlay
from gui import gui_handle as handle
from functools import partial
from gui.widgets.event_filter import EventFilter
from gui.widgets.edit_overlay import EditOverlay
import qtawesome as fa


class ProofOverlay(QtWidgets.QWidget):
    def __init__(self, parent, img):
        super(ProofOverlay, self).__init__(parent)
        self.ui = Ui_MainOverlay()
        self.ui.setupUi(self)

        # Vars
        self.parent = parent
        self.image = img
        self.session = img.session
        self.add_proof = self.ui.proof.text()
        self.proofs = self.image.proofs
        self.loose = self.load_proofs()[0]
        self.proof = self.load_proofs()[1]
        self.selection = None
        self.edit_overlay = EditOverlay
        self.filter = EventFilter(self)
        self.preview_icon = fa.icon('fa.search', color='black')
        self.delete_icon = fa.icon('fa.ban', color='red')
        self.logo_icon = fa.icon('fa.image', color="black")

        # Connections
        self.ui.loose_proof.mousePressEvent = (partial(self.select, self.loose))
        self.ui.proof.mousePressEvent = (partial(self.select, self.proof))
        self.ui.create.clicked.connect(self.func_control)

        # Event Filter
        self.ui.loose_proof.setProperty("action", "proof_context")
        self.ui.loose_proof.setProperty("loose", True)
        self.ui.loose_proof.installEventFilter(self.filter)
        if self.proof is not None:
            self.ui.proof.setProperty("action", "proof_context")
            self.ui.proof.installEventFilter(self.filter)
        print(f"PROOF DEFAULT - {self.proof}")

        # Setup
        self.load_image()
        self.ui.crop_box.setHidden(True)

    def load_image(self):
        self.ui.image_name.setText(self.image.display)
        self.ui.image.setPixmap(QtGui.QPixmap(self.image.thumb).scaled(200, 200, QtCore.Qt.KeepAspectRatio))

    def load_proofs(self):
        self.proofs = self.image.proofs
        proof = None
        loose = None
        for p in self.proofs:
            if p.loose is True:
                loose = p
            else:
                proof = p
        self.ui.loose_proof.setPixmap(QtGui.QPixmap(loose.thumb).scaled(350, 350, QtCore.Qt.KeepAspectRatio))
        self.ui.loose_label.setText(f"Loose Proof ({loose.size})")
        if proof is not None:
            self.ui.proof.setProperty("Image", True)
            self.ui.proof.setProperty("action", "proof_context")
            self.ui.proof.setStyle(self.ui.proof.style())
            self.ui.proof.setPixmap(QtGui.QPixmap(proof.thumb).scaled(350, 350, QtCore.Qt.KeepAspectRatio))
        else:
            self.ui.proof.setProperty("Image", False)
            self.ui.proof.clear()
            self.ui.proof.setText(self.add_proof)
            self.ui.proof.setStyle(self.ui.proof.style())
        return loose, proof

    def view(self):
        print(f"CURRENT SELECTION: {self.selection}")
        handle.view_img(self.selection)

    def select(self, img, e):
        self.loose = self.load_proofs()[0]
        self.proof = self.load_proofs()[1]
        self.ui.crop_box.setHidden(False)
        if img == self.loose:
            self.ui.create.setProperty("func", "crop_loose")
            self.ui.create.setText('Edit Loose')
        elif img == self.proof:
            self.ui.create.setProperty("func", "create_proof")
            self.ui.create.setText('Create Proof')
        self.selection = img

    def func_control(self):
        p = self.ui.create.property("func")
        if p == "create_proof":
            self.create_proof()
        elif p == "crop_loose":
            self.crop_loose()

    def create_proof(self):
        size = self.ui.crop.currentText()
        if size != "Photoshop" and size != "None":
            self.image.proof(self.session, size, loose=False)
        self.ui.crop_box.setHidden(True)
        self.proof = self.load_proofs()[1]
        self.ui.proof.setProperty("action", "proof_context")

    def delete_proof(self):
        self.ui.proof.setProperty("action", "none")
        self.proof.delete()
        self.load_proofs()

    def crop_loose(self):
        size = self.ui.crop.currentText()
        self.image.edit_loose(self.loose, size)
        self.ui.crop_box.setHidden(True)
        self.loose = self.load_proofs()[0]

    def edit_proof(self):
        #self.parent.setGeometry(QtCore.QRect(0, 0, 1200, 1200))
        self.parent.edit_proofs(self, self.proof)

    def close(self):
        self.parent.close_preview(self)
