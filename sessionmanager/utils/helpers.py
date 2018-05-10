# Program: Session Manager
# File: helpers.py
# Desc: Helper functions
# Author: Braden Mars


import time
import os

# Get Date (MonthYear) TODO: REMOVE THIS FUNCTION AND USAGES AND THE ONE BELOW IT
def get_month_year(num=False):
    if num:
        date = "%s/%s/%s" % (time.strftime("%m"), (time.strftime("%d")), time.strftime("%Y"))
    else:
        date = "%s%s" % (time.strftime("%B"), time.strftime("%Y"))
    return date


def get_today():
    date = "%s %s, %s" % (time.strftime("%B"), time.strftime("%d"), time.strftime("%Y"))
    return date


def translate_date(date):
    text = date.strftime(f"%B %d, %Y")
    return str(text)


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


def get_dng(dir):
    files = []
    for file in os.listdir(dir):
        if file.endswith(".dng"):
            files.append(file)
    return files


# Chunk Generator
def chunk(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


# Determines best number of chunks to split files into
def chunk_factor(files):
    factor = len(files)
    if factor < 20:
        return 2
    else:
        return False


