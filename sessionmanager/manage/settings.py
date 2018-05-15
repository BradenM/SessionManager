# Program: Session Manager
# File: manage/settings.py
# Desc: Setting Classes
# Author: Braden Mars

from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean, Table, ForeignKey, ARRAY
from data.base import Base, engine
from sqlalchemy.orm import relationship
import manage.manage as m
from data import data


class Setting(Base):
    # Database Info
    __tablename__ = "settings"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)
    logos = relationship('Logo', backref="options", cascade="all, delete-orphan")

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


class Logo(Base):
    # Database Info
    __tablename__ = "options"
    id = Column(Integer, primary_key=True)
    setting_id = Column(Integer, ForeignKey('settings.id'))
    setting = relationship('Setting')
    name = Column(String)
    path = Column(String)
    thumb = Column(String)

    def __init__(self, setting, name, path, proof):
        self.setting = setting
        self.name = name
        self.path = path
        self.thumb = self.make_thumb(proof)

    def make_thumb(self, proof):
        thumb = m.thumb(self, proof)
        return thumb


Base.metadata.create_all(engine)

if len(data.iterate_table(Setting)) < 1:
    m.setup_settings(Setting)