# Program: Session Manager
# File: data/data_old.py
# Desc: SQLAlchemy Base
# Author: Braden Mars

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from definitions import DATABASE


engine = create_engine(f'sqlite:///{DATABASE}', echo=False)
Base = declarative_base()

