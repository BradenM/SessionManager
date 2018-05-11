# Program: Session Manager
# File: utils/image.py
# Desc: Photoshop Bridge and Image Processing
# Author: Braden Mars

import subprocess
import os
from PIL import Image


# AppleScript
def applescript(ascript):

    osa = subprocess.Popen(['osascript', '-'],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
    stdout, stderr = osa.communicate(ascript)
    return osa.returncode, stdout, stderr


def as_quote(astr):

    astr = astr.replace('"', '" & quote & "')
    return '"{}"'.format(astr)


# Open Image in Photoshop
def ps_open(path):
    script = '''
    tell application "Adobe Photoshop CC 2018"
    set filePath to "{fp}"
    open alias filePath as Camera RAW
    end tell'''.format(fp=path)
    applescript(script)


def translate_size(size):
    sizes = {
        '5x7': (1500, 2100)
    }
    if size in sizes.keys():
        return sizes[size]
    else:
        raise AttributeError


# Crop Image
def crop_image(path, size):
    img_path = os.path.split(path)
    img_name = os.path.splitext(img_path[1])
    pixels = translate_size(size)
    img = Image.open(path)
    width = img.size[0]/2
    height = img.size[1]/2
    crop = img.crop(
        (
            width - pixels[0],
            height - pixels[1],
            width + pixels[0],
            height + pixels[1],
        )
    )
    crop.save(f"{img_path[0]}/{img_name[0]}_{size}{img_name[1]}")