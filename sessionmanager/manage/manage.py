# Program: Session Manager
# File: manage/handle.py
# Desc: Backend for sessions
# Author: Braden Mars

import os
import subprocess
from shutil import copyfile, rmtree
from utils import helpers as h, validate as v
from data import data_old
from definitions import ROOT, SESSIONS
import multiprocessing as mp
from rawkit.raw import Raw
from data import data
#from manage.image import Image

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
    os.mkdir(session_path)
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


# Save session to database
def save_session(session):
    data.add_row(session)


# Delete Session
def delete_session(inst):
    rmtree(inst.path)
    data.del_row(inst)


# Check if session name exist
def session_exist(inst, name):
    ex = data.row_exists(inst, name)
    return ex


''' ---- IMAGES ----'''

# Get File Info


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


