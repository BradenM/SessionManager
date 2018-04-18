# Program: Session Manager
# File: data/data.py
# Desc: Manage Data
# Author: Braden Mars

from utils import helpers as h, validate as v
from definitions import ROOT, DATABASE
import sqlite3

# Session Table
id = "ID"
id_type = "INTEGER PRIMARY KEY"
name = "Name"
name_type = "TEXT"
path = "Path"
path_type = "TEXT"
create_date = "CreationDate"
create_date_type = "TEXT"
file_count = "FileCount"
file_count_type = "INTEGER"
desc = "Description"
desc_type = "TEXT"
has_raw = "HasRaw"
has_raw_type = "TEXT"
modified_date = "LastModified"
modified_date_type = "TEXT"

# Files Table
f_id = "ID"
f_id_type = "INTEGER PRIMARY KEY"
s_name = "SessionName"
s_name_type = "TEXT"
f_name = "FileName"
f_name_type = "TEXT"
f_display = "DisplayName"
f_display_type = "TEXT"
position = "Position"
position_type = "TEXT"
f_path = "Path"
f_path_type = "TEXT"
f_jpg_path = "JPG_Path"
f_jpg_path_type = "TEXT"
f_modified_date = "LastModified"
f_modified_date_type = "TEXT"


def connect():
    global conn
    global db
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = lambda cursor, row: row[0]
    db = conn.cursor()


def close():
    conn.commit()
    conn.close()


def create_db():
    connect()
    s_query = "CREATE TABLE sessions ({id} {idt}, {n} {nt}, {path} {patht}, {cd} {cdt}, {fc} {fct}, {d} {dt}, " \
              "{hr} {hrt}, {md} '{mdt}')"\
        .format(id=id, idt=id_type, n=name, nt=name_type, path=path, patht=path_type, cd=create_date,
                cdt=create_date_type, fc=file_count, fct=file_count_type, d=desc, dt=desc_type, hr=has_raw,
                hrt=has_raw_type, md=modified_date, mdt=modified_date_type)
    db.execute(s_query)
    conn.commit()

    f_query = "CREATE TABLE files ({id} {id_type}, {sid} {sidt}, {n} {nt}, {pos} {post}, {p} {pt}, {jpg} {jpgt}, {dn} {dnt}, {m} {mt})"\
        .format(id=f_id, id_type=f_id_type, sid=s_name, sidt=s_name_type, n=f_name, nt=f_name_type,
                pos=position, post=position_type, p=f_path, pt=f_path_type, jpg=f_jpg_path, jpgt=f_jpg_path_type,
                dn=f_display, dnt=f_display_type, m=f_modified_date, mt=f_modified_date_type)
    db.execute(f_query)
    close()


def add_session(name, path, count, desc, raw):
    connect()
    date = h.get_today()
    query = "INSERT INTO sessions VALUES (NULL, '{n}', '{p}', '{d}', '{c}', '{desc}', '{r}', '{md}')".format(n=name, p=path,
                                                                                                      d=date, c=count,
                                                                                                      desc=desc, r=raw, md=None)
    print(query)
    db.execute(query)
    close()


def add_files(session, name, pos, path):
    connect()
    query = "INSERT INTO files VALUES (NULL, '{sn}', '{n}', '{p}', '{pa}', '{j}', '{dn}', '{m}')".format(sn=session, n=name, p=pos, pa=path, j=None, dn=name, m=None)
    db.execute(query)
    close()


def retrieve_data(table, name=None, column=None, string=False, iterate=False):
    connect()
    if table == "sessions":
        col = "Name"
    else:
        table = "files"
        col = "FileName"
    if iterate:
        query = "SELECT {c} FROM '{t}'".format(c=col, t=table)
    else:
        query = "SELECT {c} FROM '{t}' WHERE {col}='{n}'".format(c=column, t=table, col=col, n=name)
    print(query)
    db.execute(query)
    data = db.fetchall()
    if string:
        try:
            path = ''.join(data[0])
        except IndexError:
            close()
            return False
        close()
        return path
    else:
        close()
        return data


def get_realname(display_name):
    connect()
    query = "SELECT FileName FROM files WHERE DisplayName='{dn}'".format(dn=display_name)
    db.execute(query)
    data = db.fetchall()
    name = ''.join(data[0])
    close()
    return name


def update_data(table, column, update, check_column, check_data):
    connect()
    query = "UPDATE '{t}' SET {c}=('{up}') WHERE {cc}=('{cd}')".format(t=table, c=column, up=update, cc=check_column,
                                                                         cd=check_data)
    print(query)
    db.execute(query)
    close()


def delete_session(name):
    connect()
    query = "DELETE FROM sessions WHERE Name='{s}'".format(s=name)
    db.execute(query)
    query = "DELETE FROM files WHERE SessionName='{s}'".format(s=name)
    db.execute(query)
    close()


if v.check_db() is False:
    print('called')
    create_db()
