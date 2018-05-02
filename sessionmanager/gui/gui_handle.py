# Program: Session Manager
# File: gui/gui_handle.py
# Desc: Handles GUI updates
# Author: Braden Mars

from data import data
from utils import shop_bridge, helpers as h
from definitions import ROOT_DIR
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import os


""" MAIN WINDOW """


# Grabs UI info from session
def session_info(cls, name):
    s = data.get_row(cls, name)
    if s.modify_date == s.create_date:
        modify = "Never"
    else:
        modify = s.modify_date.strftime(f"%B %d, %Y")
    create = s.create_date.strftime(f"%B %d, %Y")
    if s.has_raw:
        raw = "Yes"
    else:
        raw = "No"
    info = [s.name, create, s.desc, str(s.file_count), raw, modify]
    return info

""" ---- CREATE WINDOW ---- """


# Update Images in List
def update_images(dir):
    images = []
    for file in os.listdir(dir):
        if file.lower().endswith(".cr2"):
            images.append(file)
    items = []
    for x in images:
        item = QtWidgets.QListWidgetItem()
        icon = "%s/icons/raw.png" % ROOT_DIR
        item.setIcon(QtGui.QIcon(icon))
        item.setText(x)
        items.append(item)
    return images, items


""" ---- MANAGE WINDOW ---- """


def get_images(inst, pos):
    images = inst.images
    imgs = []
    for img in images:
        if img.position == pos:
            imgs.append(img)
    return imgs


def update_pos(inst, pos):
    data.update_row(inst, "position", pos)


def update_modify(inst):
    data.update_row(inst, "modify", date.today())




