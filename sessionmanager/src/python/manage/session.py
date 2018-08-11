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
from manage.settings import Setting
import os
from shutil import copyfile
from utils import helpers
from pathlib import Path


class Session(Base):
    # Database Information
    __tablename__ = "sessions"
    __dir__ = (Setting.get('Session Directory')).path
    id = Column(Integer, primary_key=True)
    name = Column(String)
    path = Column(String)
    create_date = Column(DateTime)
    file_count = Column(Integer)
    desc = Column(String)
    has_raw = Column(Boolean)
    modify_date = Column(DateTime)
    images = relationship('Image', backref="sessions",
                          cascade="all, delete-orphan")

    def __init__(self, name, raw_path, desc='', keep_raw=False, auto_create=True):
        self.name = name
        self.rawpath = raw_path
        self.has_raw = keep_raw
        self.path = ""
        self.desc = ""
        self.file_count = 0
        d = datetime.now()
        self.modify_date = d
        self.create_date = d
        self.setup(auto_create)

    # Functions

    def setup(self, auto_create):
        self.path = m.structure(self)
        m.copy_raw(self.rawpath, self.path)
        if auto_create:
            self.create(None)

    def create(self, prog_callback):
        m.convert_raw(self.path, prog_callback)
        if not self.has_raw:
            m.delete_raw(self.path)
        m.rename_files(self.path, self.name)
        for img in list(self.path.glob('*.dng')):
            image = Image(self, img.name)
            self.images.append(image)
        self.file_count = len(self.images)
        self.generate_thumbs()
        self.save()

    @staticmethod
    def delete(inst):
        m.delete_session(inst)

    def save(self):
        self.path = str(self.path)
        m.save(self)

    def generate_thumbs(self):
        for img in self.images:
            tpath = m.raw_thumbify(img.path)
            img.thumb = tpath

    def update_migration(self, origin, path):
        sessions = data.iterate_table(Session)
        images = data.iterate_table(Image)
        proofs = data.iterate_table(Proof)
        all = [sessions, images, proofs]
        m.migrate_update(origin, path, all)

    def to_dict(self):
        data = {
            'name': self.name,
            'raw_path': self.has_raw,
            'path': self.path,
            'desc': self.desc,
            'file_count': self.file_count,
            'create_date': helpers.translate_date(self.create_date),
            'modify_date': helpers.translate_date(self.modify_date),
            'cover_img': Path(self.images[0].thumb).name
        }
        return data

    @classmethod
    def all(self):
        return data.iterate_table(Session)

    def __str__(self):
        return f"Session: {self.name} - {self.desc} - {self.create_date}"

    def __repr__(self):
        return f"Session: {self.name} - {self.desc} - {self.create_date}"


class Image(Base):
    # Database Info
    __tablename__ = "files"
    __dir__ = Session.__dir__
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
    proofs = relationship('Proof', backref="proofs",
                          cascade="all, delete-orphan")

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

    def gen_proof(self, session, size="5x7", loose=True):
        proof = m.make_proof(self, session, size, loose)
        if loose is not True:
            p = Proof(self, f"proof_{proof[0]}",
                      proof[1], size, loose, proof[2])
        else:
            p = Proof(self, proof[0], proof[1], size, loose, proof[2])
        self.proofs.append(p)
        m.save(self)

    def edit_loose(self, loose, size):
        m.delete_img(loose)
        self.gen_proof(self.session, size)

    def export_proof(self, path):
        export_path = os.path.join(path, self.session.name)
        proof_path = os.path.join(export_path, "Proofs")
        loose_path = os.path.join(export_path, "Loose Proofs")
        if not os.path.exists(export_path):
            os.mkdir(export_path)
            os.mkdir(proof_path)
            os.mkdir(loose_path)
        for p in self.proofs:
            if p.loose:
                p.export(loose_path)
            else:
                p.export(proof_path)
        return export_path


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
        self.active = False

    def delete(self):
        m.delete_img(self)

    def update(self):
        m.update_proof(self)

    def export(self, path):
        export_path = os.path.join(path, self.name)
        copyfile(self.path, export_path)


Base.metadata.create_all(engine)
