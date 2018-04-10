# Program: Session Manager
# File: helpers.py
# Desc: Helper functions
# Author: Braden Mars


import time
import os
from data import data

# Get Date (MonthYear)
def get_month_year(num=False):
    if num:
        date = "%s/%s/%s" % (time.strftime("%m"), (time.strftime("%d")), time.strftime("%Y"))
    else:
        date = "%s%s" % (time.strftime("%B"), time.strftime("%Y"))
    return date


# Remove Whitespace
def remove_whitespace(string):
    new_str = string.replace(' ', '')
    return new_str


# Convert Array to string
def data_to_string(data):
    string = ''.join(data[0])
    return string


# Strip Extension
def strip_ext(filename, thumb=False, undo=False):
    name, ext = os.path.splitext(filename)
    if thumb:
        if undo:
            name = name + ext
            return name
        name = name.replace('_thumb', '')
    return name


# Check if image as a JPG
def has_jpg(file_name):
    path = data.retrieve_data("files", name=file_name, column="JPG_Path", string=True)
    if path.__len__() < 5:
        return False
    else:
        return path
