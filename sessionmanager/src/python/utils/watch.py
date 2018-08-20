# Program: Session Manager
# File: utils/watch,py
# Desc: WatchDog Classes
# Author: Braden Mars

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os

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
    def __init__(self, observer, detect_callback):
        super(WatchMount, self).__init__()
        self.observer = observer
        self.callback = detect_callback
    patterns = ["*"]

    def process(self, event):
        if event.event_type == 'created':
            print(event.src_path, event.event_type, event.is_directory)
            if os.path.ismount(event.src_path):
                self.callback.emit(str(event.src_path))

    def on_created(self, event):
        # if self.skip:
        #     self.process(event)
        # else:
        #     self.process(event)
        #     print('STOPPING')
        #     self.observer.stop()
        self.process(event)


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


def watch_mount(detect_callback):
    observer = Observer()
    path = "/Volumes"
    observer.schedule(WatchMount(observer, detect_callback), path=path)
    observer.start()
    try:
        while observer.isAlive():
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
