# Program: Session Manager
# File: manage/session.py
# Desc: Session classes
# Author: Braden Mars

import manage.manage as m
import data.data as d


class Session(object):

    parent_dir = "sessions"
    dng = "/Applications/Adobe\ DNG\ Converter.app/Contents/MacOS/Adobe\ DNG\ Converter"

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
    def create(self):
        name = self.name
        rawpath = self.rawpath
        keepraw = self.keepraw
        desc = self.description
        dng = self.dng

        path = m.structure(name)
        m.copy_raw(rawpath, path)
        m.convert_raw(dng, path)
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
        



        
        
        


        


       
        


