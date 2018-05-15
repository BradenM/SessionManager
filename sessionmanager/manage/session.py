# Program: Session Manager
# File: manage/session.py
# Desc: Session classes
# Author: Braden Mars


from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean, Table, ForeignKey
from data.base import Base, engine
from sqlalchemy.orm import relationship
from datetime import datetime
import manage.manage as m
from data import data
import os


class Session(Base):
    # Database Information
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    path = Column(String)
    create_date = Column(DateTime)
    file_count = Column(Integer)
    desc = Column(String)
    has_raw = Column(Boolean)
    modify_date = Column(DateTime)
    images = relationship('Image', backref="sessions", cascade="all, delete-orphan")

    def __init__(self, name=None):
        self.name = name
        self.rawpath = ""
        self.has_raw = False
        self.path = ""
        self.desc = ""
        self.file_count = 0
        d = datetime.now()
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
            if img.endswith(".dng"):
                image = Image(self, img)
                self.images.append(image)
        self.file_count = len(self.images)

    @staticmethod
    def delete(inst):
        m.delete_session(inst)

    def save(self):
        m.save(self)

    @staticmethod
    def generate_thumbs(inst, callback, thumb_call):
        m.gen_thumbs(inst, callback, thumb_call)


class Image(Base):
    # Database Info
    __tablename__ = "files"
    id = Column(Integer, primary_key=True)
    session = relationship('Session')
    session_id = Column(Integer, ForeignKey('sessions.id'))
    name = Column(String)
    path = Column(String)
    display = Column(String)
    position = Column(String)
    thumb = Column(String)
    jpg = Column(String)
    active = Column(Boolean)
    active_file = Column(String)
    modify = Column(Date)
    proofs = relationship('Proof', backref="proofs", cascade="all, delete-orphan")

    def __init__(self, session, name):
        self.session = session
        self.session_path = session.path
        self.name = name
        self.path = "%s/%s" % (self.session_path, self.name)
        display = self.name.rstrip(".dng")
        self.display = display
        self.position = "RAW"
        self.thumb = ""
        self.jpg = ""
        self.modify = datetime.now()
        self.active_file = ""
        self.active = False

    def set_active(self, state):
        data.update_row(self, "active", state)

    def check(self, path):
        img = m.check_jpg(self, path)
        print("JPG LOCATE REPLY - %s" % img.name)
        return img

    def set_jpg(self, path):
        data.update_row(self, "active_file", path)
        print("SET JPG REPLY -- ")
        print(self.active_file)

    def finalize(self, session):
        m.setup_proof(self, session)
        m.finalize_img(self, session)
        m.update_thumb(self)

    def proof(self, session, size="5x7", loose=True):
        proof = m.make_proof(self, session, size, loose)
        if loose is not True:
            p = Proof(self, f"proof_{proof[0]}", proof[1], size, loose, proof[2])
        else:
            p = Proof(self, proof[0], proof[1], size, loose, proof[2])
        self.proofs.append(p)
        m.save(self)

    def edit_loose(self, loose, size):
        m.delete_img(loose)
        self.proof(self.session, size)


class Proof(Base):
    # Database Info
    __tablename__ = "proofs"
    id = Column(Integer, primary_key=True)
    image_id = Column(Integer, ForeignKey('files.id'))
    name = Column(String)
    path = Column(String)
    loose = Column(Boolean)
    modify = Column(Date)
    thumb = Column(String)
    size = Column(String)
    scale = Column(String)

    def __init__(self, image, name, path, size, loose, thumb):
        self.name = name
        self.path = path
        self.loose = loose
        self.modify = datetime.now()
        self.thumb = thumb
        self.size = size
        self.scale = ""

    def delete(self):
        m.delete_img(self)


Base.metadata.create_all(engine)
