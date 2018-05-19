# Program: Session Manager
# File: detect.py
# Desc: Detects USB and Opens Prompt
# Author: Braden Mars

from gui import app
from manage.usb import USB


def main():
    detect = USB()
    if detect.watch():
        start(detect.path)


def start(path):
    app.start_usb(path)


if __name__ == '__main__':
    main()
