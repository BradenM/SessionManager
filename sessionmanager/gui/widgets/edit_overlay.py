# Program: Session Manager
# File: gui/widgets/edit_overlay.py
# Desc: Overlay for editing proofs
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.logo_crop_overlay_ui import Ui_EditOverlay
from gui import gui_handle as handle
from gui.widgets.logo_item import QLogoItem
from manage.settings import Setting, Logo
from gui.widgets.event_filter import EventFilter
from functools import partial


class EditOverlay(QtWidgets.QWidget):
    def __init__(self, parent, proof):
        super(EditOverlay, self).__init__(parent)
        self.ui = Ui_EditOverlay()
        self.ui.setupUi(self)

        # Vars
        self.parent = parent
        self.image = proof
        self.setting = Setting
        self.active_item = self.active()
        #self.scene = EditScene(self, self.ui.edit_view, self.active_item)
        self.preview = handle.preview_proof(self.image)
        self.logo_setting = self.setting.get('Logos')
        self.logos = self.logo_setting.logos
        self.filter = EventFilter(self)
        self.filter.logo_added.connect(self.insert_logo)
        # Connections
        #self.ui.logo_list.itemClicked.connect(self.add_logo)
        self.ui.logo_list.installEventFilter(self.filter)
        self.ui.logo_list.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        # Setup
        self.load_image()
        self.populate_logo()

    # Functions
    def insert_logo(self, obj):
        item = obj.currentItem()
        logo = item.data(QtCore.Qt.UserRole)
        pix = QtGui.QPixmap(logo.thumb)
        self.ui.edit_view.insert_logo(pix)

    def active(self, widget=False):
        try:
            item = self.ui.logo_list.currentItem().data(QtCore.Qt.UserRole)
            self.active_item = item
            if widget is True:
                item = self.ui.logo_list.currentItem()
                return self.ui.logo_list.itemWidget(item)
            return item
        except AttributeError:
            pass

    def load_image(self):
        pix = QtGui.QPixmap(self.preview)
        # img = QtWidgets.QGraphicsPixmapItem()
        # img.setPixmap(pix)
        # self.scene.addItem(img)
        # #self.scene.addItem(logo)
        # self.active()
        # self.ui.edit_view.setScene(self.scene)

        self.ui.edit_view.set_photo(pix)
        #self.ui.edit_view.toggle_drag()

    def populate_logo(self):
        self.ui.logo_list.clear()
        for logo in self.logos:
            widget = QLogoItem(logo)
            item = QtWidgets.QListWidgetItem(self.ui.logo_list)
            item.setSizeHint(widget.size())
            item.setData(QtCore.Qt.UserRole, logo)
            self.ui.logo_list.addItem(item)
            self.ui.logo_list.setItemWidget(item, widget)
        widget = QLogoItem()
        item = QtWidgets.QListWidgetItem(self.ui.logo_list)
        item.setData(QtCore.Qt.UserRole, "empty")
        item.setSizeHint(widget.size())
        self.ui.logo_list.addItem(item)
        self.ui.logo_list.setItemWidget(item, widget)

    def add_logo(self):
        item = self.active()
        if item == "empty":
            try:
                logo_file = handle.setup_logo(self)
                logo = Logo(self.logo_setting,  logo_file[0], logo_file[1], self.image)
                self.logo_setting.add(logo)

            except FileNotFoundError:
                pass
        else:
            pass
        self.populate_logo()

