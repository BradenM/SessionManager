# Program: Session Manager
# File: sessionmanager.py (Core)
# Desc: Session Manage Core
# Author: Braden Mars

import sqlalchemy
import sqlalchemy.sql.default_comparator
import sqlalchemy.ext.baked
import definitions
from api import api


def main():
    api.start()


if __name__ == '__main__':
    main()
