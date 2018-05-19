# Program: Session Manager
# File: manage/usb_pop.py
# Desc: USB Class for AutoDetecting Memory Cards
# Author: Braden Mars

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from data.base import Base, engine
from data import data
from manage import manage as m
import os
from utils import watch
import usb.core
import usb.util


class USB(Base):
    # Database info
    __tablename__ = "usb"
    id = Column(Integer, primary_key=True)
    #vendorid = Column(String)
    #productid = Column(String)
    #manufacturer = Column(String)
    #serial = Column(String)
    path = Column(String)
    active = Column(Boolean)

    def watch(self):
        watch.watch_mount(callback=self.scan)
        return True

    def stop(self):
        return True

    def scan(self, path):
        files = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(path)) for f in fn if f.lower().endswith('.txt')]
        if len(files) <= 0:
            print('No Files')
        else:
            print("Contains RAW files:")
            print(files)
            self.path = path
            self.stop()

    def save(self):
        m.save(self)

    @staticmethod
    def info():
        print('called')
        ignore = ['Apple Inc.', 'Apple Computer, Inc.']
        devices = usb.core.find(find_all=True)
        active = []
        if devices is not None:
            for d in devices:
                manu = usb.util.get_string(d, d.iManufacturer)
                if manu not in ignore and manu is not None:
                    print(manu)
