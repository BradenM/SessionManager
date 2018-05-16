# Program: Session Manager
# File: utils/image.py
# Desc: Photoshop Bridge and Image Processing
# Author: Braden Mars

import subprocess
import os
from PIL import Image, ImageOps


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
        '5x7': (1500, 2100),
        '4x4': (1200, 1200),
        'edit': (595, 595),
        'item': (200, 200),
        'logo': (130, 130),
        'proof': (350, 350)
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
    thumb = ImageOps.fit(crop, (350, 350), Image.ANTIALIAS)
    output = f"{img_path[0]}/{img_name[0]}_{size}{img_name[1]}"
    thumb_output = f"{img_path[0]}/{img_name[0]}_thumb{img_name[1]}"
    crop.save(output)
    thumb.save(thumb_output)
    return output, thumb_output


def crop_proof(path, size, output):
    pixels = translate_size(size)
    thumb_size = translate_size('proof')
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
    thumb = ImageOps.fit(crop, thumb_size, Image.ANTIALIAS)
    os.remove(output)
    thumb.save(output)


# View Image
def view_external(path):
    img = Image.open(path)
    img.show('JPEG')


# Create Thumbnail of JPEG
def thumb_jpg(path, output, scale=None):
    img = Image.open(path)
    if scale is not None:
        x, y = scale.split(',')
        print(f"{float(x) * 0.01} ==> {img.size[0]}")
        scale_x = ((float(x) * 0.01) * int(img.size[0]))
        scale_y = (float(y) * 0.01) * int(img.size[1])
        down_scale = (scale_x, scale_y)
        print(down_scale)
    else:
        down_scale = translate_size("5x7")
    img.thumbnail(down_scale, Image.ANTIALIAS)
    img.save(output)


# Create Temporary Edit JPEG
def jpg_preview(path, output, size):
    pixels = translate_size(size)
    img = Image.open(path)
    scale_x = (pixels[0] / img.size[0]) * 100
    scale_y = (pixels[1] / img.size[1]) * 100
    scale = f"{scale_x},{scale_y}"
    print(scale)
    preview = ImageOps.fit(img, pixels, Image.ANTIALIAS)
    preview.save(output, 'JPEG', quality=95)
    return scale

# Scale Image
def scale():
    pass
