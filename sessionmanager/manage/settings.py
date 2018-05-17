# Program: Session Manager
# File: manage/settings_mod.py
# Desc: Setting Classes
# Author: Braden Mars

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from data.base import Base, engine
import manage.manage as m
from definitions import SESSIONS
from data import data


class Setting(Base):
    # Database Info
    __tablename__ = "settings"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)
    type = Column(String)
    __mapper_args__ = {'polymorphic_on': type}

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    @staticmethod
    def get(name):
        option = data.get_row(Setting, name)
        return option

    def add(self, inst):
        m.save(inst)

    def save(self):
        m.save(self)


class General(Setting):
    # Database Info
    __tablename__ = 'general'
    __mapper_args__ = {'polymorphic_identity': 'general'}
    id = Column(Integer, ForeignKey('settings.id'), primary_key=True)
    state = Column(Boolean)

    def __init__(self, name, desc, state):
        super(General, self).__init__(name, desc)
        self.state = state


class Storage(Setting):
    # Database Info
    __tablename__ = 'storage'
    __mapper_args__ = {'polymorphic_identity': 'storage'}
    id = Column(Integer, ForeignKey('settings.id'), primary_key=True)
    path = Column(String)

    def __init__(self, name, desc, path):
        super(Storage, self).__init__(name, desc)
        self.path = path


class Logo(Setting):
    # Database Info
    __tablename__ = "logo"
    __mapper_args__ = {'polymorphic_identity': 'logo'}
    id = Column(Integer, ForeignKey('settings.id'), primary_key=True)
    path = Column(String)
    thumb = Column(String)

    def __init__(self, name, desc, path, proof):
        super(Logo, self).__init__(name, desc)
        self.path = path
        self.thumb = self.make_thumb(proof)

    def make_thumb(self, proof):
        thumb = m.thumb(self, proof)
        return thumb


Base.metadata.create_all(engine)

DEFAULT = {
    Storage:
        {
            ("Session Directory", "A Path to Store Session files in", SESSIONS),
        },
    General:
        {
            ("Auto Detect", "Enable/Disable Automatic Detection of Camera memory card", True),
        }
}

if len(data.iterate_table(Setting)) < 1:
    m.setup_settings(DEFAULT)
