# Program: Session Manager
# File: definitions.py
# Desc: Definitions
# Author: Braden Mars

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(ROOT_DIR, 'sessionmanager.py')

DATABASE = '%s/database.sqlite' % ROOT_DIR
SESSIONS = '%s/sessions' % ROOT_DIR
UI = '%s/gui/ui' % ROOT_DIR

DNG = "/Applications/Adobe\ DNG\ Converter.app/Contents/MacOS/Adobe\ DNG\ Converter"
