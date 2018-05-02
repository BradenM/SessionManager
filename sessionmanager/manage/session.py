# Program: Session Manager
# File: manage/session.py
# Desc: Session classes
# Author: Braden Mars


from sqlalchemy import Column, String, Integer, Date, Boolean, Table, ForeignKey
from data.base import Base, engine
from sqlalchemy.orm import relationship
from datetime import date
import manage.manage as m
import os

class Session(Base):
    # Database Information
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    path = Column(String)
    create_date = Column(Date)
    file_count = Column(Integer)
    desc = Column(String)
    has_raw = Column(Boolean)
    modify_date = Column(Date)
    images = relationship('Image', backref="sessions", cascade="all, delete-orphan")

    def __init__(self, name=None):
        self.name = name
        self.rawpath = ""
        self.has_raw = False
        self.path = ""
        self.desc = ""
        self.file_count = 0
        d = date.today()
        self.modify_date = d
        self.create_date = d
        if name is not None:
            self.path = m.get_path(name)

    # Functions

    def setup(self, raw_path, desc, raw):
        self.rawpath = raw_path
        self.desc = desc
        self.has_raw = raw

        self.path = m.structure(self.name)
        print(self.path)
        m.copy_raw(self.rawpath, self.path)

    def create(self, prog_callback):
        m.convert_raw(self.path, prog_callback)
        if self.has_raw is not True:
            m.delete_raw(self.path)
        m.rename_files(self.path)
        for img in os.listdir(self.path):
            image = Image(self, img)
            self.images.append(image)
        self.file_count = len(self.images)

    def add_image(self, img):
        if img not in self.images:
            self.images.append(img)

    @staticmethod
    def delete(inst):
        m.delete_session(inst)

    def save(self):
        m.save_session(self)

    @staticmethod
    def generate_thumbs(inst, callback, thumb_call):
        m.gen_thumbs(inst, callback, thumb_call)


class Image(Base):
    # Database Info
    __tablename__ = "files"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('sessions.id'))
    name = Column(String)
    path = Column(String)
    display = Column(String)
    position = Column(String)
    thumb = Column(String)
    jpg = Column(String)
    modify = Column(Date)

    def __init__(self, session, name):
        self.session = session.name
        self.session_path = session.path
        self.name = name
        self.path = "%s/%s" % (self.session_path, self.name)
        display = self.name.rstrip(".dng")
        self.display = display
        self.position = "RAW"
        self.thumb = ""
        self.jpg = ""
        self.modify = date.today()

Base.metadata.create_all(engine)
