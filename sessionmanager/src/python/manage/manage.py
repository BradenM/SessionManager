# Program: Session Manager
# File: manage/manage.py
# Desc: Backend for sessions
# Author: Braden Mars

import os
import subprocess
from shutil import copyfile, rmtree, copytree
from utils import helpers as h, image
import multiprocessing as mp
from rawkit.raw import Raw
from data import data
from definitions import DNG
from pathlib import Path


# Structure Session
def structure(inst):
    # Base - (Session Dir, Date, Name)
    session_path = Path(inst.__dir__) / h.get_month_year() / \
        h.remove_whitespace(inst.name)
    paths = [
        session_path,
        session_path / 'final',
        session_path / 'proof',
        session_path / 'thumb'
    ]
    for path in paths:
        os.makedirs(path, exist_ok=True)
    return session_path


# Iterate Files
def iterate_files(path, ext):
    count = []
    for file in os.listdir(path):
        if file.endswith(ext):
            count.append(file)
    return count


# Copy Raw Files
def copy_raw(raw_path, path, callback):
    count = len([i for i in os.listdir(raw_path)
                 if i.lower().endswith('.cr2')])
    for file in os.listdir(raw_path):
        if file.lower().endswith(".cr2"):
            copyfile("%s/%s" % (raw_path, file), "%s/%s" %
                     (path, file.lower()))
            if callback is not None:
                callback('copy', (file, count))
    if callback is not None:
        callback((file, count), complete=True)


# Convert RAW to DNG MP
def convert(chunk, path):
    os.chdir(path)
    count = len([i for i in os.listdir(path) if i.lower().endswith('.cr2')])
    for file in chunk:
        p = subprocess.Popen(f"{DNG} -c {file}", shell=True)
        p.wait()
    return (chunk, count)


# Convert RAW to DNG
def convert_raw(path, callback):
    raw = [file for file in os.listdir(
        path) if file.lower().endswith('.cr2')]
    workers = mp.cpu_count()
    chunk_f = h.chunk_factor(raw)
    if chunk_f is False:
        chunk_f = workers
    chunks = list(h.chunk(raw, chunk_f))
    pool = mp.Pool(workers)
    jobs = []
    for x in chunks:
        print('Process Called')
        jobs.append(pool.apply_async(convert, args=(x, path)))
    for j in jobs:
        val = j.get()
        if callback is not None:
            callback('convert', data=val)
    pool.close()
    pool.join()
    if callback is not None:
        callback(('', len(raw)), complete=True)


# Delete CR2 files
def delete_raw(path):
    for file in list(path.glob('*.cr2')):
        os.remove("%s/%s" % (path, file.name))


# Rename Files
def rename_files(path, name):
    files = [file for file in list(path.glob('*.dng'))]
    for count, file in enumerate(files):
        new = str(path / (f'{h.remove_whitespace(name)}_{count}.dng'))
        os.rename(str(file), new)


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


# Settings


# Create Settings
def setup_settings(settings):
    for cls in settings:
        for args in settings[cls]:
            s = cls(*args)
            s.save()


def add_logo(inst):
    inst.setting.add(inst)


def check_dir(path):
    if os.path.exists(path):
        return False
    else:
        return True


def migrate_sessions(inst, session_dir, path):
    if os.path.exists(session_dir):
        try:
            copytree(session_dir, path)
        except Exception as e:
            print(f"Failed to copy directories - {e}")
            return False
    else:
        if check_dir(path):
            data.update_row(inst, "path", path)
            inst.save()
            return True
        else:
            return False
    return True


def migrate_update(origin, new_p, rows):
    for cls in rows:
        for inst in cls:
            parent = os.path.dirname(inst.path)
            head = f"{os.path.split(os.path.split(parent)[0])[1]}/{os.path.basename(parent)}"
            new_path = f"{new_p}/{head}/{inst.name}"
            print(new_path)
            data.update_row(inst, "path", new_path)
            try:
                thead = f"{os.path.split(os.path.split(inst.thumb)[0])[1]}/{os.path.basename(inst.thumb)}"
                tpath = f"{new_p}/{thead}"
                data.update_row(inst, "thumb", tpath)
            except AttributeError:
                print(f'No Thumbs Found for {inst.name}')
    try:
        rmtree(origin)
    except Exception as e:
        print(f"Could not remove origin directory - {e}")

    return True


# Images


# Generate thumb from raw file
def raw_thumbify(path):
    with Raw(path) as raw:
        path = Path(path)
        export = path.parent / 'thumb'
        thumb = str(export / path.name.replace('.dng', '_thumb.jpg'))
        raw.save_thumb(thumb)
    return thumb


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
