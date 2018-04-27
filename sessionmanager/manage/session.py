# Program: Session Manager
# File: manage/session.py
# Desc: Session classes
# Author: Braden Mars

import manage.manage as m


class Session(object):

    parent_dir = "sessions"

    def __init__(self, name=None):
        self.name = name
        self.rawpath = ""
        self.description = "desc"
        self.keepraw = False
        self.path = ""
        if name is not None:
            self.path = m.get_path(name)

    # Static Methods
    @staticmethod
    def list():
        sessions = m.iterate_sessions()
        return sessions

    # Functions
    def exist(self):
        check = m.session_exist(self.name)
        return check

    def setup(self, raw_path, desc, raw):
        self.rawpath = raw_path
        self.description = desc
        self.keepraw = raw

        self.path = m.structure(self.name)
        print(self.path)
        m.copy_raw(self.rawpath, self.path)

    def create(self, prog_callback):
        m.convert_raw(self.path, prog_callback)
        if self.keepraw is not True:
            m.delete_raw(self.path)
        m.rename_files(self.path)
        file_cnt = m.iterate_files(self.path, ".dng")
        m.save_session(self.name, self.path, file_cnt, self.description, self.keepraw)

    def info(self):
        info = m.get_session(self.name)
        return info

    def delete(self):
        name = self.name
        m.delete_session(name)
        

class Thumb(Session):

    def generate(self, callback):
        m.gen_thumbs(self.path, callback)

    def get(self):
        thumbs = m.get_thumbs(self.name)
        return thumbs

        
        


        


       
        


