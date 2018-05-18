# Program: Session Manager
# File: data/data_old.py
# Desc: SQLAlchemy Base
# Author: Braden Mars

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


engine = create_engine('sqlite:///database.sqlite', echo=False)
Base = declarative_base()

