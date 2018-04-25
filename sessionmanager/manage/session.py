# Program: Session Manager
# File: manage/session.py
# Desc: Session classes
# Author: Braden Mars

import manage.manage as m
import data.data as d
from definitions import DNG


class Session(object):

    parent_dir = "sessions"

    def __init__(self, name):
        self.name = name
        self.rawpath = ""
        self.description = "desc"
        self.keepraw = False

    # Attributes
    def raw_path(self, rawpath):
        self.rawpath = rawpath

    def desc(self, description):
        self.description = description

    def keep_raw(self, keepraw):
        self.keepraw = keepraw

    # Functions
    def create(self, prog_callback):
        name = self.name
        rawpath = self.rawpath
        keepraw = self.keepraw
        desc = self.description

        path = m.structure(name)
        m.copy_raw(rawpath, path)
        m.convert_raw(path, prog_callback)
        if keepraw:
            pass
        else:
            m.delete_raw(path)
        m.rename_files(path)
        # Save
        file_cnt = m.iterate_files(path, ".dng")
        m.save_session(name, path, file_cnt, desc, keepraw)
    
    def delete(self):
        name = self.name
        m.delete_session(name)
        



        
        
        


        


       
        


