# Program: Session Manager
# File: data/validate.py
# Desc: Validate Data
# Author: Braden Mars

import os
from definitions import ROOT
from definitions import DATABASE
from definitions import SESSIONS


# Check if sessions exist
def check_sessions():
    if os.path.isdir(SESSIONS):
        return True
    else:
        return False


# Check if parent exist
def check_parent(parent):
    par_dir = "%s/%s" % (SESSIONS, parent)
    if os.path.isdir(par_dir):
        return True
    else:
        return False


def check_db():
    if os.path.isfile(DATABASE):
        return True
    else:
        return False

