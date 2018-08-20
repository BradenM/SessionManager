# Program: Session Manager
# File: data/data.py
# Desc: DB Engine, Session & Functions
# Author: Braden Mars

from sqlalchemy.orm import sessionmaker
from data.base import engine

# Engine and Session Creation
DatabaseSession = sessionmaker(bind=engine)
db = DatabaseSession()


# Get all rows in a table
def iterate_table(cls):
    table = []
    for row in db.query(cls).all():
        table.append(row)
    return table


# Get a specific row by name
def get_row(cls, name, attr=None):
    if attr is None:
        attr = "name"
    for row in db.query(cls).filter(getattr(cls, f"{attr}") == name).all():
        return row


# Grab First Row where
def first_row(cls):
    for row in db.query(cls).first():
        return row


# Gets Rows WHERE
def get_rows(cls, name, attr=None):
    rows = []
    if attr is None:
        attr = "name"
    for row in db.query(cls).filter(getattr(cls, f"{attr}") == name).all():
        rows.append(row)
    print(rows)
    return rows


# Add row (Instance) to table
def add_row(inst):
    db.add(inst)
    db.commit()


# Delete Row
def del_row(inst):
    db.delete(inst)
    db.commit()


# Check if row exist
def row_exists(cls, name):
    row = db.query(cls).filter(cls.name == name).exists()
    result = db.query(row).scalar()
    return result


# Update Row
def update_row(inst, a, up):
    getattr(inst, a)
    setattr(inst, a, up)
    db.commit()
