# Program: Session Manager
# File: manage/settings.py
# Desc: Setting Classes
# Author: Braden Mars

from sqlalchemy import Column, String, Integer, ForeignKey
from data.base import Base, engine
import manage.manage as m
from data import data


class Setting(Base):
    # Database Info
    __tablename__ = "settings"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)
    discriminator = Column('type', String)
    __mapper_args__ = {'polymorphic_on': discriminator}

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


class Storage(Setting):
    # Database Info
    __tablename__ = 'storage'
    __mapper_args__ = {'polymorphic_identity': 'storage'}
    id = Column(Integer, ForeignKey('settings.id'), primary_key=True)
    path = Column(String)


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

# if len(data.iterate_table(Setting)) < 1:
#     m.setup_settings(Setting)