# Program: Session Manager
# File: gui/gui_handle.py
# Desc: Handles GUI updates
# Author: Braden Mars

from data import data
from manage import handle
from gui.dialogs.popup import Popup
from definitions import ROOT
from PyQt5 import QtGui, QtWidgets
import os


# Iterate Sessions from database
def iterate_sessions():
    sessions = data.retrieve_data("sessions", column='Name', iterate=True)
    print(sessions)
    items = []
    for x in sessions:
        item = QtWidgets.QListWidgetItem()
        item.setText(x)
        items.append(item)
    return items


def get_info(name):
    date = data.retrieve_data("sessions", name, column='CreationDate', string=True)
    desc = data.retrieve_data("sessions", name, column="Description", string=True)
    return date, desc


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
        icon = "icons/cr2.png"
        item.setIcon(QtGui.QIcon(icon))
        item.setText(x)
        items.append(item)
    return images, items



def check_name_exist(name):
    check = data.retrieve_data("sessions", name=name, column="Name")
    if len(check) <= 0:
        return False
    else:
        return True


