# Program: Session Manager
# File: definitions.py
# Desc: Definitions
# Author: Braden Mars

import os
import debug
from pathlib import Path

if debug.LIVE is False:
    ROOT_DIR = Path.cwd()
    if debug.NATIVE:
        ROOT_DIR = ROOT_DIR / 'src' / 'python'
    ROOT = ROOT_DIR / 'main.py'
else:
    ROOT_DIR = os.path.expanduser('~/.sessionmanager')
    ROOT = os.path.join(ROOT_DIR, 'main.py')

DATABASE = str(ROOT_DIR / 'database.sqlite')
UI = '%s/gui/ui' % ROOT_DIR
ICONS = os.path.join(ROOT_DIR, "icons")
SESSIONS = os.path.join(ROOT_DIR, "sessions")
# DNG = "/Applications/Adobe\ DNG\ Converter.app/Contents/MacOS/Adobe\ DNG\ Converter"
DNG = 'WINEPREFIX="$HOME/wine-dng" wine "$HOME/wine-dng/drive_c/Program Files/Adobe/Adobe DNG Converter/Adobe DNG Converter.exe"'

# App Definitions
NAME = "Session Manager"
VERSION = "1.0.0"
DESC = "An application for photographers to easily manage their sessions"
