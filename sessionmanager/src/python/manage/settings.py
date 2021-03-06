# Program: Session Manager
# File: manage/settings_mod.py
# Desc: Setting Classes
# Author: Braden Mars

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from data.base import Base, engine
import manage.manage as m
from definitions import SESSIONS, DNG, ICONS
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
    __tab__ = "General"
    __icon__  = f"{ICONS}/settings/gen.png"
    __winicon__ = f"{ICONS}/settings/gen_title.png"
    __mapper_args__ = {'polymorphic_identity': 'general'}
    id = Column(Integer, ForeignKey('settings.id'), primary_key=True)
    state = Column(Boolean)

    def __init__(self, name, desc, state):
        super(General, self).__init__(name, desc)
        self.state = state


class Storage(Setting):
    # Database Info
    __tablename__ = 'storage'
    __tab__ = "Storage"
    __icon__ = f"{ICONS}/settings/stor.png"
    __winicon__ = f"{ICONS}/settings/stor_title.png"
    __mapper_args__ = {'polymorphic_identity': 'storage'}
    id = Column(Integer, ForeignKey('settings.id'), primary_key=True)
    path = Column(String)
    default = Column(String)

    def __init__(self, name, desc, path):
        super(Storage, self).__init__(name, desc)
        self.path = path
        self.default = path

    def migrate(self, session_dir, path):
        result = m.migrate_sessions(self, session_dir, path)
        return result


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
            ("Session Directory", "A Path to Store Session files in\nDefault: In App Directory", SESSIONS),
            ("DNG Converter", "Path to the Adobe DNG Converter", DNG)
        },
    General:
        {
            ("Auto Detect", "Enable/Disable Automatic Detection of Camera memory card", True),
        }
}

if len(data.iterate_table(Setting)) < 1:
    m.setup_settings(DEFAULT)
