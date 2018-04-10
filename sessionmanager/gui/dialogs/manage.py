# Program: Session Manager
# File: gui/dialogs/manage.py
# Desc: Manage Session Window
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from definitions import ROOT_DIR
from gui.ui.managewindow_ui import Ui_Manage
from gui import gui_handle as handle
from gui.threads.manage_thumbs import ManageThumbs
from gui.threads.watch_directory import WatchDirectory


class ManageWindow(QtWidgets.QDialog):
    def __init__(self, name):
        super(ManageWindow, self).__init__()
        self.ui = Ui_Manage()
        self.ui.setupUi(self)
        self.name = name
        # Setup
        _, _, self.path = handle.get_info(self.name)
        global gif
        gif = QtGui.QMovie("%s/icons/loading.gif" % ROOT_DIR)
        self.ui.preview_label.hide()
        self.ui.preview_loader.setMovie(gif)
        self.ui.preview_loader.hide()
        self.ui.preview_text.hide()
        self.ui.proof_button.setDisabled(True)
        self.ui.proofInfo.hide()
        self.ui.update_proof.hide()
        self.ui.finalize_proof.setDisabled(True)
        self.update_thumbs()

        # Connections
        self.ui.thumb_slider.itemClicked.connect(self.preview_image)
        self.ui.proof_button.clicked.connect(self.make_proof)
        self.ui.open_proof.clicked.connect(self.open_proof)
        self.ui.proof_thumbs.itemClicked.connect(self.proof_info)
        self.ui.finalize_proof.clicked.connect(self.finalize_proof)
        self.ui.export_button.clicked.connect(self.export_final)

    # Functions
    def update_thumbs(self):
        def working():
            gif.start()
            self.ui.preview_loader.show()
            self.ui.preview_text.show()

        def finished():
            gif.stop()
            self.ui.preview_loader.hide()
            self.ui.preview_text.hide()
            self.ui.preview_label.show()

        self.ui.thumb_slider.clear()
        self.ui.proof_thumbs.clear()
        self.ui.final_thumbs.clear()
        self.get_thread = ManageThumbs(self.path)
        self.get_thread.working.connect(working)
        self.get_thread.raw.connect(self.ui.thumb_slider.addItem)
        self.get_thread.proof.connect(self.ui.proof_thumbs.addItem)
        self.get_thread.final.connect(self.ui.final_thumbs.addItem)
        self.get_thread.finished.connect(finished)
        self.get_thread.start()

    def preview_image(self):
        self.ui.proof_button.setDisabled(False)
        thumb = self.ui.thumb_slider.currentItem().text()
        size = self.ui.preview_label.size()
        preview = handle.get_preview(self.path, thumb, size)
        self.ui.preview_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.preview_label.setPixmap(preview)

    def make_proof(self):
        thumb = self.ui.thumb_slider.currentItem().text()
        name = self.ui.rename_text.text()
        handle.update_pos(self.path, thumb, "PROOF", name=name)
        self.ui.rename_text.clear()
        self.update_thumbs()

    def proof_info(self):
        self.ui.proofInfo.show()
        thumb = self.ui.proof_thumbs.currentItem().text()
        file_name, mod_date = handle.get_proof_info(thumb)
        self.ui.name_edit.setText(thumb)
        self.ui.file_name.setText(file_name)
        self.ui.file_date.setText(mod_date)
        if mod_date != "None":
            self.ui.finalize_proof.setDisabled(False)

    def open_proof(self):
        thumb = self.ui.proof_thumbs.currentItem().text()
        handle.script_open_proof(self.path, thumb)
        self.watch_thread = WatchDirectory(self.path)
        self.watch_thread.start()

    def finalize_proof(self):
        thumb = self.ui.proof_thumbs.currentItem().text()
        handle.update_pos(self.path, thumb, "FINAL")
        handle.finalize(self.path, thumb)
        self.update_thumbs()

    def export_final(self):
        ex_path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select a Directory"))
        items = []
        for index in range(self.ui.final_thumbs.count()):
            items.append(self.ui.final_thumbs.item(index).text())
        handle.export(self.path, items, ex_path)
