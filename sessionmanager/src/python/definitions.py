# Program: Session Manager
# File: definitions.py
# Desc: Definitions
# Author: Braden Mars

import os
import sys
import debug

if debug.LIVE is False:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT = os.path.join(ROOT_DIR, 'sessionmanager.py')
else:
    ROOT_DIR = os.path.expanduser('~/.sessionmanager')
    ROOT = os.path.join(ROOT_DIR, 'sessionmanager.py')

DATABASE = os.path.join(ROOT_DIR, "database.sqlite")
UI = '%s/gui/ui' % ROOT_DIR
ICONS = os.path.join(ROOT_DIR, "icons")
SESSIONS = os.path.join(ROOT_DIR, "sessions")
# DNG = "/Applications/Adobe\ DNG\ Converter.app/Contents/MacOS/Adobe\ DNG\ Converter"
DNG = 'dng'

# App Definitions
NAME = "Session Manager"
VERSION = "1.0.0"
DESC = "An application for photographers to easily manage their sessions"
