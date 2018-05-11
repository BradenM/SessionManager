# Program: Session Manager
# File: data/data.py
# Desc: DB Engine, Session & Functions
# Author: Braden Mars

from sqlalchemy.orm import sessionmaker
from data.base import engine

# Engine and DBSession Creation
DatabaseSession = sessionmaker(bind=engine)
dbs = DatabaseSession()


# Get all rows in a table
def iterate_table(cls):
    table = []
    for row in dbs.query(cls).all():
        table.append(row)
    return table


# Get a specific row by name
def get_row(cls, name, attr=None):
    if attr is None:
        attr = "name"
    for row in dbs.query(cls).filter(getattr(cls, f"{attr}") == name).all():
        return row


# Gets Rows WHERE
def get_rows(cls, name, attr=None):
    rows = []
    if attr is None:
        attr = "name"
    for row in dbs.query(cls).filter(getattr(cls, f"{attr}") == name).all():
        rows.append(row)
    print(rows)
    return rows


# Add row (Instance) to table
def add_row(inst):
    dbs.add(inst)
    dbs.commit()


# Delete Row
def del_row(inst):
    dbs.delete(inst)
    dbs.commit()


# Check if row exist
def row_exists(cls, name):
    row = dbs.query(cls).filter(cls.name == name).exists()
    result = dbs.query(row).scalar()
    return result


# Update Row
def update_row(inst, a, up):
    getattr(inst, a)
    setattr(inst, a, up)
    dbs.commit()
