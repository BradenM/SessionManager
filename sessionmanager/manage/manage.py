# Program: Session Manager
# File: manage/manage.py
# Desc: Backend for sessions
# Author: Braden Mars

import os
import subprocess
from shutil import copyfile, rmtree
from utils import helpers as h, validate as v, image
from definitions import ROOT, SESSIONS
import multiprocessing as mp
from rawkit.raw import Raw
from data import data

cwd = os.getcwd()
date = h.get_month_year()
parent = "%s" % date
DNG = "/Applications/Adobe\ DNG\ Converter.app/Contents/MacOS/Adobe\ DNG\ Converter"

db = None


# Structure Session
def structure(name):
    if v.check_sessions() is False:
        os.mkdir(SESSIONS)
    os.chdir(SESSIONS)
    if v.check_parent(parent) is False:
        os.mkdir("%s" % date)
    global session_name
    session_name = h.remove_whitespace(name)
    session_path = "%s/%s" % (parent, session_name)
    final_path = f"{session_path}/final"
    proof_path = f"{session_path}/proof"
    os.mkdir(session_path)
    os.mkdir(final_path)
    os.mkdir(proof_path)
    path = "%s/sessions/%s" % (cwd, session_path)
    return path


# Get Path
def get_path(name):
    session_name_path = h.remove_whitespace(name)
    session_path = "%s/%s" % (parent, session_name_path)
    path = "%s/sessions/%s" % (cwd, session_path)
    if os.path.isdir(path):
        return path
    else:
        return False


# Iterate Files
def iterate_files(path, ext):
    count = []
    for file in os.listdir(path):
        if file.endswith(ext):
            count.append(file)
    return count


# Copy Raw Files
def copy_raw(raw_path, path):
    for file in os.listdir(raw_path):
        if file.lower().endswith(".cr2"):
            copyfile("%s/%s" % (raw_path, file), "%s/%s" % (path, file))


# Convert RAW to DNG MP
def convert(chunk, path):
    os.chdir(path)
    for file in chunk:
        p = subprocess.Popen("%s %s" % (DNG, file), shell=True)
        p.wait()
    return chunk


# Convert RAW to DNG
def convert_raw(path, update):
    raw = []
    for file in os.listdir(path):
        if file.lower().endswith(".cr2"):
            raw.append(file)
    workers = mp.cpu_count()
    chunk_f = h.chunk_factor(raw)
    if chunk_f is False:
        chunk_f = workers
    chunks = list(h.chunk(raw, chunk_f))
    pool = mp.Pool(workers)
    for x in chunks:
        print('Process Called')
        pool.apply_async(convert, args=(x, path), callback=update)
    pool.close()
    pool.join()


# Delete CR2 files
def delete_raw(path):
    for file in os.listdir(path):
        if file.lower().endswith(".cr2"):
            os.remove("%s/%s" % (path, file))


# Rename Files
def rename_files(path):
    os.chdir(path)
    files = iterate_files(path, ".dng")
    for count, file in enumerate(files):
        if file.endswith(".dng"):
            os.rename(file, "%s_%s.dng" % (session_name, count))


# Save instance to database
def save(inst):
    data.add_row(inst)


# Delete Session
def delete_session(inst):
    data.del_row(inst)
    rmtree(inst.path)


# Check if session name exist
def session_exist(inst, name):
    ex = data.row_exists(inst, name)
    return ex


# Create Settings
def setup_settings(settings):
    for cls in settings:
        for args in settings[cls]:
            s = cls(*args)
            s.save()


def add_logo(inst):
    inst.setting.add(inst)


''' ---- IMAGES ----'''


# Generate Thumbs
def gen_thumbs(inst, callback, thumb_call):
    os.chdir(inst.path)
    if os.path.isdir('thumbs'):
        return False
    os.mkdir('thumbs')
    files = h.get_dng(inst.path)
    thumbs = {}
    for file in files:
        with Raw(file) as raw:
            name = file.replace(".dng", "_thumb.jpg")
            raw.save_thumb(name)
            thumbs[file] = name
        callback.emit(1)
        os.rename(name, "thumbs/%s" % name)
    thumb_call.emit(thumbs)


# Check JPG
def check_jpg(img, path):
    jpg_name = os.path.splitext(os.path.basename(path))[0]
    active_imgs = data.get_rows(type(img), 1, "active")
    for img in active_imgs:
        img_name = os.path.splitext(img.name)[0]
        print(f"COMPARE: {jpg_name} <===> {img_name}")
        if jpg_name == img_name:
            return img
    return False


# Update Thumb
def update_thumb(img):
    os.remove(img.thumb)
    image.thumb_jpg(img.jpg, img.thumb)
    print(f'Thumb failed, image must be a proof: {img.name}')
    image.thumb_jpg(img.path, img.thumb)


def thumb(inst, proof):
    name = os.path.split(inst.path)
    thumb_name = f"{name[0]}/thumb_{name[1]}"
    if os.path.isfile(thumb_name):
        os.remove(thumb_name)
    image.thumb_jpg(inst.path, thumb_name, proof.scale)
    return thumb_name


# Add Image to finals
def finalize_img(img, session):
    final_path = f"{session.path}/final"
    img_name = os.path.splitext(img.display)[0]
    jpg_path = f'{final_path}/{img_name}.jpg'
    os.rename(img.active_file, jpg_path)
    data.update_row(img, "position", "FINAL")
    data.update_row(img, "jpg", jpg_path)
    data.update_row(img, "active", 0)
    data.update_row(img, "active_file", "")
    print(f"{img.name} finalized ===> {jpg_path}")
    img.gen_proof(session)


# Setup Proof
def setup_proof(img, session):
    proof_dir = f"{session.path}/proof/{img.name}"
    if os.path.isdir(proof_dir) is False:
        os.mkdir(proof_dir)
    else:
        print("Proof Folder Already Created")


# Create Proof
def make_proof(img, session, size, loose):
    path = image.crop_image(img.jpg, size)
    name = os.path.basename(path[0])
    thumb_name = os.path.basename(path[1])
    proof_path = f"{session.path}/proof/{img.name}/{name}"
    thumb_path = f"{session.path}/proof/{img.name}/{thumb_name}"
    if loose is not True:
        proof_path = f"{session.path}/proof/{img.name}/proof_{name}"
        thumb_path = f"{session.path}/proof/{img.name}/proof_{thumb_name}"
    for p in path:
        p_name = os.path.basename(p)
        p_path = f"{session.path}/proof/{img.name}/{p_name}"
        if loose is not True:
            p_path = f"{session.path}/proof/{img.name}/proof_{p_name}"
        os.rename(p, p_path)
    return name, proof_path, thumb_path


# Update Proof
def update_proof(proof):
    size = proof.size
    image.crop_proof(proof.path, size, proof.thumb)


# Delete Image/Proof
def delete_img(img):
    os.remove(img.path)
    os.remove(img.thumb)
    data.del_row(img)
