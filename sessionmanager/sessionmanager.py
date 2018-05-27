# Program: Session Manager
# File: sessionmanager.py (Core)
# Desc: Session Manage Core
# Author: Braden Mars

from PyQt5 import *
import sqlalchemy
import sqlalchemy.sql.default_comparator
import sqlalchemy.ext.baked
import definitions
from gui import app


def main():
    app.start()


if __name__ == '__main__':
    main()
