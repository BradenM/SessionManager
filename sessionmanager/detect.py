# Program: Session Manager
# File: detect.py
# Desc: Detects USB and Opens Prompt
# Author: Braden Mars

from gui import app
from manage.usb import USB
import time


def main():
    detect = USB(thread=True)
    while True:
        time.sleep(1)
        if detect.found:
            print(detect.path)
            print(detect.files)
            start(detect)


def start(inst):
    app.start_usb(inst)


if __name__ == '__main__':
    main()
