# Program: Session Manager
# File: gui/gui_handle.py
# Desc: Handles GUI updates
# Author: Braden Mars

from data import data
from utils import image, helpers as h
from definitions import ROOT_DIR, SESSIONS
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from shutil import copy
import os


""" MAIN WINDOW """


# Grabs UI info from session
def session_info(s):
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
    if pos == "PROOF":
        pos = "FINAL"
    for img in images:
        if img.position == pos:
            imgs.append(img)
    return imgs


def get_proofs(img, loose):
    proofs = img.proofs
    imgs = []
    print(proofs)
    for p in proofs:
        imgs.append(p)

    print('GET PROOFS')
    print(imgs)
    return imgs


def update_img(inst, pos):
    data.update_row(inst, "position", pos)
    data.update_row(inst, "modify", datetime.now())


def open_img(session, img):
    image.ps_open(img)


def get_actives(img):
    active_imgs = data.get_rows(type(img), 1, "active")
    return active_imgs


def view_img(img):
    image.view_external(img.path)


def preview_proof(proof):
    path = os.path.split(proof.path)
    out = f"{path[0]}/prev_{path[1]}"
    if os.path.isfile(out):
        os.remove(out)
    scale = image.jpg_preview(proof.path, out, "edit")
    data.update_row(proof, "scale", str(scale))
    return out


def setup_logo(parent):
    dialog = QtWidgets.QFileDialog.getOpenFileName(parent, "Select a Logo")
    path = str(dialog[0])
    print(f"HERE -- {path}")
    logo_dir = f"{SESSIONS}/logo"
    name = os.path.split(path)[1]
    if os.path.isdir(logo_dir) is False:
        os.mkdir(logo_dir)
    logo = f"{logo_dir}/{name}"
    copy(path, logo)
    return name, logo


def get_settings(cls):
    general = [x for x in data.get_rows(cls, "general", "type")]
    storage = [x for x in data.get_rows(cls, "storage", "type")]
    return general, storage
