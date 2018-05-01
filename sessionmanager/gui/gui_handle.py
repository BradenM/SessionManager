# Program: Session Manager
# File: gui/gui_handle.py
# Desc: Handles GUI updates
# Author: Braden Mars

from data import data_old
from data import data
from utils import process, helpers as h
from definitions import ROOT_DIR
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import os
from shutil import copy

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


def get_thumbs(inst, pos):
    images = inst.images
    thumbs = {}
    for img in images:
        if img.position == pos:
            thumbs[img.name] = img.thumb
    return thumbs


def update_pos(inst, name, pos):
    images = inst.images
    cls = type(images[0])
    img = data.get_row(cls, name)
    data.update_row(img, "position", pos)
