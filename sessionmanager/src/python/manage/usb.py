# Program: Session Manager
# File: manage/usb_pop.py
# Desc: USB Class for AutoDetecting Memory Cards
# Author: Braden Mars

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, ARRAY
from data.base import Base, engine
from data import data
from manage import manage as m
import os
from utils import watch
import usb.core
import usb.util
import threading
from PyQt5.QtCore import *


class Signals(QObject):
    usb_detected = pyqtSignal(str)


class USB(QRunnable):
    # Database info
    __tablename__ = "usb"
    id = Column(Integer, primary_key=True)
    mount = Column(String)
    path = Column(String)
    active = Column(Boolean)

    def __init__(self, interval=1, self_thread=False, *args, **kwargs):
        super(USB, self).__init__()
        self.files = ""
        self.interval = interval
        self.found = False
        self.signals = Signals()
        kwargs['detect_callback'] = self.signals.usb_detected
        self.kwargs = kwargs
        if self_thread:
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = True
            thread.start()

    def watch(self):
        watch.watch_mount(**self.kwargs)
        return True

    @pyqtSlot()
    def run(self):
        # result = self.watch()
        # self.found = result
        self.watch()

    def stop(self):
        return True

    def scan(self, path):
        files = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(path)) for f in fn if f.lower().endswith('.cr2')]
        if len(files) <= 0:
            print('No Files')
            return False
        else:
            print("Contains RAW files:")
            print(len(files))
            parent = os.path.dirname(files[0])
            self.path = parent
            self.files = files
            self.found = True
            return parent

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
