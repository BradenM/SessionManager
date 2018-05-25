# Program: Session Manager
# File: /sessionmanager/gui/widgets/popup.py
# Desc: Popup Widget
# Author: Braden Mars

from PyQt5.QtWidgets import *


class PopupMsg(QMessageBox):
    F_ERROR = 0
    E_INPUT = 1

    def __init__(self, parent, type, detail=None):
        super(PopupMsg, self).__init__(parent)
        self.type = type
        self.detail = detail
        self.title = "Session Manager"

        # Setup
        if type == self.F_ERROR:
            self.finalize_error()
        if type == self.E_INPUT:
            self.export_popup()

    def finalize_error(self):
        self.setWindowTitle(self.title)
        self.setText('Cannot Finalize image yet.')
        self.setInformativeText('You have not saved your image as a JPG yet. Please finish in Photoshop before finalizing.')
        self.setStandardButtons(self.Ok | self.Retry)
        retry = self.button(self.Retry)
        retry.setText('Reopen')
        self.setDefaultButton(self.Ok)
        self.setDetailedText(str(self.detail))
        self.setIcon(self.Warning)
        self.exec_()
        if self.clickedButton() == retry:
            return True

    def export_popup(self):
        self.setWindowTitle(self.title)
        self.setText("What would you like to export?")
        self.setInformativeText("Select an option then choose a directory to save your images too.")
        self.setStandardButtons(self.Ok | self.Yes | self.No | self.Cancel)
        loose = self.button(self.Ok)
        proof = self.button(self.Yes)
        all = self.button(self.No)
        loose.setText("Loose Proofs")
        proof.setText("Proofs")
        all.setText("Both")
        self.setIcon(self.Question)
        self.setDefaultButton(self.Cancel)
        self.exec_()
        if self.clickedButton() == loose:
            return 1
        if self.clickedButton() == proof:
            return 2
        if self.clickedButton() == all:
            return 3


