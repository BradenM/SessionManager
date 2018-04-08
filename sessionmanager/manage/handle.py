# Program: Session Manager
# File: manage/handle.py
# Desc: Handler for Sessions
# Author: Braden Mars

from manage import session


def create(name, raw_path, desc, keep_raw):
    s = session.Session(name)
    s.raw_path(raw_path)
    s.desc(desc)
    s.keep_raw(keep_raw)
    s.create()


def delete(name):
    s = session.Session(name)
    s.delete()