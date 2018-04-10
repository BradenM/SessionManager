# Program: Session Manager
# File: utils/watch,py
# Desc: Watches directory for photoshop file save
# Author: Braden Mars

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from gui import gui_handle as handle


class WatchExport(PatternMatchingEventHandler):
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
            handle.update_proof(event.src_path)


    def on_created(self, event):
        self.process(event)


def watch(path):
    observer = Observer()
    s_path = path
    observer.schedule(WatchExport(), path=s_path)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

