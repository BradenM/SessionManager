# Program: Session Manager
# File: gui/gui_handle.py
# Desc: Handles GUI updates
# Author: Braden Mars

from data import data
from utils import image, helpers as h
from definitions import ROOT_DIR
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import os


""" MAIN WINDOW """


# Grabs UI info from session
def session_info(cls, name):
    s = data.get_row(cls, name)
    if s.modify_date == s.create_date:
        modify = "Never"
    elif s.modify_date.time() != s.create_date.time() and s.modify_date.date() == s.create_date.date():
        modify = "Today"
    else:
        modify = h.translate_date(s.modify_date)
    create = s.create_date.strftime(f"%B %d, %Y")
    if s.has_raw:
        raw = "Yes"
    else:
        raw = "No"
    info = [s.name, create, s.desc, str(s.file_count), raw, modify]
    return info


def recent_session(cls):
    sessions = data.iterate_table(cls)
    return min(sessions, key=lambda x: abs(x.modify_date - datetime.now()))

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


def session_modify(inst):
    data.update_row(inst, "modify_date", datetime.now())


def get_images(inst, pos):
    images = inst.images
    imgs = []
    for img in images:
        if img.position == pos:
            imgs.append(img)
    return imgs


def update_img(inst, pos):
    data.update_row(inst, "position", pos)
    data.update_row(inst, "modify", datetime.now())


def open_img(session, img):
    image.ps_open(img.path)


def get_actives(img):
    active_imgs = data.get_rows(type(img), 1, "active")
    return active_imgs



