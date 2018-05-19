# Program: Session Manager
# File: utils/watch,py
# Desc: WatchDog Classes
# Author: Braden Mars

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


# Watch for PhotoShop Export
class WatchExport(PatternMatchingEventHandler):
    def __init__(self, observer, callback, single):
        super(WatchExport, self).__init__()
        self.callback = callback
        self.observer = observer
        self.single = single
    patterns = ["*.jpg", "*.jpeg"]

    def process(self, event):
        if event.event_type == "created":
            print(event.src_path, event.event_type)
            self.callback.emit(event.src_path)

    def on_created(self, event):
        self.process(event)
        if self.single:
            self.observer.stop()


# Watch for device mounts
class WatchMount(PatternMatchingEventHandler):
    def __init__(self, observer, callback):
        super(WatchMount, self).__init__()
        self.observer = observer
        self.callback = callback
        self.skip = True
    patterns = ["*"]

    def process(self, event):
        if event.event_type == 'created':
            print(event.src_path, event.event_type, event.is_directory)
            self.callback(event.src_path)
            self.skip = False

    def on_created(self, event):
        if self.skip:
            self.process(event)
        else:
            self.process(event)
            print('STOPPING')
            self.observer.stop()


def watch(path, single, callback):
    observer = Observer()
    s_path = path
    observer.schedule(WatchExport(observer, callback, single), path=s_path)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def watch_mount(callback=None):
    observer = Observer()
    path = "/Volumes"
    observer.schedule(WatchMount(observer, callback), path=path)
    observer.start()
    try:
        while observer.isAlive():
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
