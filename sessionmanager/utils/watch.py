# Program: Session Manager
# File: utils/watch,py
# Desc: Watches directory for jpg file save
# Author: Braden Mars

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from gui import gui_handle as handle


class WatchExport(PatternMatchingEventHandler):
    def __init__(self, callback):
        super(WatchExport, self).__init__()
        self.callback = callback
    patterns = ["*.jpg", "*.jpeg"]

    def process(self, event):
        """
        event.event_type
            'created'
        event.is_directory
            True
        event.src_path
            '/path/'
        """
        if event.event_type == "created":
            print(event.src_path, event.event_type)
            self.callback.emit(event.src_path)

    def on_created(self, event):
        self.process(event)


def watch(path, callback):
    observer = Observer()
    s_path = path
    observer.schedule(WatchExport(callback), path=s_path)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

