# Program: Session Manager
# File: gui/gui_handle.py
# Desc: Handles GUI updates
# Author: Braden Mars

from data import data
from utils import shop_bridge, helpers as h
from definitions import ROOT_DIR
from PyQt5 import QtCore, QtGui, QtWidgets
from gui.threads.watch_directory import WatchDirectory
from datetime import date
import os


""" MAIN WINDOW """


# Grabs UI info from session
def session_info(cls, name):
    s = data.get_row(cls, name)
    if s.modify_date == s.create_date:
        modify = "Never"
    else:
        modify = h.translate_date(s.modify_date)
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


def update_img(inst, pos):
    data.update_row(inst, "position", pos)
    data.update_row(inst, "modify", date.today())


def open_img(session, img):
    shop_bridge.ps_open(img.path)


def check_jpg(path, active_images):
    file_name = os.path.basename(path)
    file_name = os.path.splitext(file_name)[0]
    for img in active_images:
        img_name = os.path.splitext(img.name)[0]
        if file_name == img_name:
            return img
        else:
            return False


def get_actives(img):
    active_imgs = data.get_rows(type(img), 1, "active")
    return active_imgs


def set_jpg(session, img, path):
    final_path = f"{session.path}/final"
    if os.path.isdir(final_path) is False:
        os.mkdir(final_path)
    print('hi')
    data.update_row(img, "active_file", path)
    print(img.active_file)


def finalize_img(session, img):
    final_path = f"{session.path}/final"
    img_name = os.path.splitext(img.name)[0]
    ext = os.path.splitext(img.active_file)[1]
    jpg_path = f'{final_path}/{img_name}.jpg'
    if os.path.isdir(final_path) is False:
        os.mkdir(final_path)
    os.rename(img.active_file, jpg_path)
    update_img(img, "FINAL")
    data.update_row(img, "jpg", jpg_path)

