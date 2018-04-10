# Program: Session Manager
# File: utils/process.py
# Desc: Process Images and AppleScript
# Author: Braden Mars

import rawpy
import imageio
import os
from definitions import ROOT
import subprocess


# Generate Thumbnails
def generate_thumbs(dir):
    os.chdir(dir)
    os.mkdir('thumbs')
    for file in os.listdir(dir):
        if file.endswith(".dng"):
            raw = rawpy.imread(file)
            rgb = raw.postprocess()
            name = file.replace(".dng", "_thumb.jpg")
            imageio.imsave(name, rgb)
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

