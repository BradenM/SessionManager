# Program: Session Manager
# File: gui/gui_handle.py
# Desc: Handles GUI updates
# Author: Braden Mars

from data import data
from manage import handle
from utils import process, helpers as h
from gui.dialogs.popup import Popup
from definitions import ROOT
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import os
from shutil import copy


# Iterate Sessions from database
def iterate_sessions():
    sessions = data.retrieve_data("sessions", column='Name', iterate=True)
    print(sessions)
    items = []
    for x in sessions:
        item = QtWidgets.QListWidgetItem()
        item.setText(x)
        icon = "icons/camera.png"
        item.setIcon(QtGui.QIcon(icon))
        items.append(item)
    return items


def get_info(name):
    date = data.retrieve_data("sessions", name, column='CreationDate', string=True)
    desc = data.retrieve_data("sessions", name, column="Description", string=True)
    path = data.retrieve_data("sessions", name, column="Path", string=True)
    count = data.retrieve_data("sessions", name, column="FileCount")
    count = str(count[0])
    raw = data.retrieve_data("sessions", name, column="HasRaw", string=True)
    modify = data.retrieve_data("sessions", name, column="LastModified", string=True)
    if raw is not '0':
        raw = 'Yes'
    else:
        raw = 'No'
    return date, desc, path, count, raw, modify


def delete_session(name):
    pop = Popup()
    delete = "Delete '%s'?" % name
    pop.setWindowTitle(delete)
    pop.ui.info.setText("WARNING:")
    pop.ui.desc.setText("Are you sure you want to delete '%s' ?" % name)
    check = pop.exec_()
    if check is 1:
        handle.delete(name)


# Create Session Dialog
def update_images(dir):
    images = []
    for file in os.listdir(dir):
        if file.endswith(".CR2"):
            images.append(file)

    items = []
    for x in images:
        item = QtWidgets.QListWidgetItem()
        icon = "icons/raw.png"
        item.setIcon(QtGui.QIcon(icon))
        item.setText(x)
        items.append(item)
    return images, items

# Check if session name exist
def check_name_exist(name):
    check = data.retrieve_data("sessions", name=name, column="Name")
    if len(check) <= 0:
        return False
    else:
        return True


# Manage Sessions

# Update Thumbs
def get_thumbs(path):
    if os.path.isdir("%s/thumbs" % path) is False:
        process.generate_thumbs(path)
    t_path, thumbs = process.iterate_thumbs(path)

    raw = []
    proof = []
    final = []
    for x in thumbs:
        file_name = h.strip_ext(x, thumb=True)
        pos = data.retrieve_data("files", name=file_name, column='Position', string=True)
        if pos == 'RAW':
            item = QtWidgets.QListWidgetItem()
            icon = "%s/%s" % (t_path, x)
            item.setIcon(QtGui.QIcon(icon))
            name = h.strip_ext(x, thumb=True)
            item.setText(name)
            item.setTextAlignment(Qt.AlignCenter)
            raw.append(item)
        elif pos == 'PROOF':
            item = QtWidgets.QListWidgetItem()
            jpg_path = h.has_jpg(file_name)
            if jpg_path is False:
                icon = "%s/%s" % (t_path, x)
            else:
                icon = jpg_path
            item.setIcon(QtGui.QIcon(icon))
            name = data.retrieve_data("files", name=file_name, column="DisplayName", string=True)
            item.setText(name)
            item.setTextAlignment(Qt.AlignCenter)
            proof.append(item)
        elif pos == 'FINAL':
            item = QtWidgets.QListWidgetItem()
            jpg_path = h.has_jpg(file_name)
            icon = jpg_path
            item.setIcon(QtGui.QIcon(icon))
            name = data.retrieve_data("files", name=file_name, column="DisplayName", string=True)
            item.setText(name)
            item.setTextAlignment(Qt.AlignCenter)
            final.append(item)
    return raw, proof, final


def get_preview(path, thumb, size):
    file = thumb + "_thumb.jpg"
    image = "%s/thumbs/%s" % (path, file)
    preview = QtGui.QPixmap(image).scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    return preview


def get_proof_info(displayname):
    file_name = data.get_realname(displayname)
    mod_date = data.retrieve_data("files", name=file_name, column="LastModified", string=True)
    if mod_date is None:
        mod_date = "Never"
    return file_name, mod_date


def update_pos(path, thumb, pos, name=None):
    # file = thumb + ".dng"
    # image = "%s/%s" % (path, file)
    if name is not None and name is not "":
        data.update_data("files", "DisplayName", name, "FileName", thumb)
        data.update_data("files", "Position", pos, "FileName", thumb)
    else:
        file_name = data.get_realname(thumb)
        print("HERE", file_name)
        data.update_data("files", "DisplayName", file_name, "FileName", file_name)
        data.update_data("files", "Position", pos, "FileName", file_name)
    print(name)


def script_open_proof(path, image):
    file_name = data.get_realname(image)
    jpg_path = h.has_jpg(file_name)
    if jpg_path is False:
        file_name = file_name + ".dng"
        file_path = path + "/%s" % file_name
    else:
        file_path = jpg_path
    print(file_path)
    script = '''
    tell application "Adobe Photoshop CC 2018"
    set filePath to "{fp}"
    open alias filePath as Camera RAW
    end tell'''.format(fp=file_path)
    process.applescript(script)


def update_proof(path):
    head, tail = os.path.split(path)
    name = h.strip_ext(tail)
    date = h.get_month_year(num=True)
    if os.path.isdir("%s/proofs" % head) is False:
        os.mkdir("%s/proofs" % head)
    jpg_path = "%s/proofs/%s" % (head, tail)
    os.rename(path, jpg_path)
    data.update_data("files", "LastModified", date, "FileName", name)
    data.update_data("files", "JPG_Path", jpg_path, "FileName", name)


def finalize(path, thumb):
    file = data.get_realname(thumb)
    file_name = file + ".jpg"
    if os.path.isdir("%s/finals" % path) is False:
        os.mkdir("%s/finals" % path)
    proof_path = "%s/proofs/%s" % (path, file_name)
    final_path = "%s/finals/%s" % (path, file_name)
    os.rename(proof_path, final_path)
    data.update_data("files", "JPG_Path", final_path, "FileName", file)


def export(path, items, ex_path):
    final_path = path + "/finals"
    names = []
    images = []
    _, s_name = os.path.split(path)
    ex_folder = ex_path + "/%s" % s_name
    os.mkdir(ex_folder)
    for x in items:
        print(x)
        image = data.get_realname(x)
        image_path = final_path + "/%s.jpg" % image
        names.append(x)
        images.append(image_path)

    for x in images:
        copy(x, ex_folder)
