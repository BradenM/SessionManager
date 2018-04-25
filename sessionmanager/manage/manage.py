# Program: Session Manager
# File: manage/handle.py
# Desc: Backend for sessions
# Author: Braden Mars

import os
import subprocess
from shutil import copyfile, rmtree
import time
from utils import helpers as h, validate as v
from data import data
from definitions import ROOT, SESSIONS
import multiprocessing as mp

cwd = os.getcwd()
date = h.get_month_year()
parent = "%s" % date
DNG = "/Applications/Adobe\ DNG\ Converter.app/Contents/MacOS/Adobe\ DNG\ Converter"

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
    return path


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
        if file.endswith(".CR2"):
            copyfile("%s/%s" % (raw_path, file), "%s/%s" % (path, file))


# Convert RAW to DNG
# def convert_raw(dng, path, prog_callback):
#     cr2 = len(iterate_files(path, ".CR2"))
#     subprocess.Popen("open -a %s --args -p2 %s/*.CR2" % (dng, path), shell=True)
#     global files
#     files = []
#     while True:
#         for file in os.listdir(path):
#             if file.endswith(".dng"):
#                 files.append("%s/%s" % (path, file))
#         if len(files) >= cr2:
#             time.sleep(1)
#             print("Finished converting")
#             break
#         else:
#             status = "Converting...(%s/%s)" % (len(files), cr2)
#             prog_callback.emit(len(files))
#             print(status)
#             files = []
#             time.sleep(2)

# Convert RAW to DNG MP
def convert(chunk, path):
    os.chdir(path)
    for file in chunk:
        p = subprocess.Popen("%s %s" % (DNG, file), shell=True)
        p.wait()
    return chunk


# Convert RAW to DNG
def convert_raw(path, prog):
    raw = []
    for file in os.listdir(path):
        if file.endswith(".CR2"):
            raw.append(file)
    workers = mp.cpu_count()
    chunk_f = h.chunk_factor(raw)
    if chunk_f is False:
        chunk_f = workers
    chunks = list(h.chunk(raw, chunk_f))
    pool = mp.Pool(workers)
    for x in chunks:
        print('Process Called')
        pool.apply_async(convert, args=(x, path,), callback=prog)
    pool.close()
    pool.join()


# Delete CR2 files
def delete_raw(path):
    for file in os.listdir(path):
        if file.endswith(".CR2"):
            os.remove("%s/%s" % (path, file))


# Rename Files
def rename_files(path):
    os.chdir(path)
    files = iterate_files(path, ".dng")
    for count, file in enumerate(files):
        if file.endswith(".dng"):
            os.rename(file, "%s_%s.dng" % (session_name, count))


# Save session to database
def save_session(name, path, count, desc, raw):
    data.add_session(name, path, len(count), desc, raw)
    for x in count:
        f_name = x.strip(".dng")
        f_path = path + "/%s" % x
        data.add_files(name, f_name, "RAW", f_path)


# Delete Session
def delete_session(name):
    path = data.retrieve_data("sessions", name, "Path", string=True)
    data.delete_session(name)
    rmtree(path)
