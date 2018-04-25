# Program: Session Manager
# File: utils/process.py
# Desc: Process Images and AppleScript
# Author: Braden Mars

import os
from utils import helpers
from definitions import ROOT
from manage import manage
import subprocess
import multiprocessing as mp
from rawkit.raw import Raw


# Generate Thumbs
def generate_thumbs(path, prog_callback):
    os.chdir(path)
    if os.path.isdir('thumbs'):
        return False
    os.mkdir('thumbs')
    files = helpers.get_dng(path)
    for file in files:
        with Raw(file) as raw:
            name = file.replace(".dng", "_thumb.jpg")
            raw.save_thumb(name)
        prog_callback.emit(1)
        os.rename(name, "thumbs/%s" % name)


# Iterate Thumbnails
def iterate_thumbs(dir):
    path = "%s/thumbs" % dir
    thumbs = []
    for file in os.listdir(path):
        if file.endswith(".jpg"):
            thumbs.append(file)
    return path, thumbs


# AppleScript
def applescript(ascript):

    osa = subprocess.Popen(['osascript', '-'],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
    stdout, stderr = osa.communicate(ascript)
    return osa.returncode, stdout, stderr


def asquote(astr):

    astr = astr.replace('"', '" & quote & "')
    return '"{}"'.format(astr)

