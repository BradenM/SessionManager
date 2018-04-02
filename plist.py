# Program: Session Manager
# File: plist.py
# Desc: Manage plist file in Session Manager
# Author: Braden Mars

# Imports
import os
import plistlib
import time

# Starting Structure
pl = {
    "Info" : {
        "SessionAmount" : 0,
        "MostRecentSession" : "Example Session",
    },


}

def getSessionData():
    from main import paths as p
    dataFile = os.path.expanduser(p['data'])
    return dataFile

def getFileData(KEY):
    path = retrieveData(KEY, CONTENT="Path")
    dataPath = path + "/info.plist"
    dataFile = os.path.expanduser(dataPath)
    return dataFile


def createList():
    dataFile = getSessionData()
    plistlib.writePlist(pl, dataFile)

def createDataList(KEY):
    dataFile = getFileData(KEY)
    plistlib.writePlist(pl, dataFile)

def modifyList(LIST, FILE):
    oldList = plistlib.readPlist(FILE)
    newList = {}
    newList.update(oldList.items())
    newList.update(LIST.items())
    plistlib.writePlist(newList, FILE)


def addSession(SESSIONNAME, PATH, PHOTOCOUNT, DESC, RAWSTAT):
    # Imports Dictionaries
    from main import date as d
    dataFile = getSessionData()

    Session = {
        SESSIONNAME : {
            "Path" : PATH,
            "CreationDate" : d['today_date'],
            "PhotoCount" : PHOTOCOUNT,
            "Description" : DESC,
            "HasRaw" : RAWSTAT,
            "LastModified" : "Never"
        },
    }

    modifyList(Session, dataFile)

def addfileData(KEY, FILENAME):
    dataFile = getFileData(KEY)
    path = retrieveData(KEY, CONTENT="Path")
    PATH = path + "/%s.dng" % FILENAME

    data = {
        FILENAME : {
            "Position" : "RAW",
            "Path" : PATH,
            "JPG_Path" : "",
        },
    }

    modifyList(data, dataFile)


def validateKey(KEY):
    dataFile = getSessionData()
    data = plistlib.readPlist(dataFile)

    if KEY in data:
        return True
    else:
        return False

def retrieveData(KEY, CONTENT=None):
    dataFile = getSessionData()
    data = plistlib.readPlist(dataFile)

    keyContent = data[KEY]
    if CONTENT is None:
        return data[KEY]
    else:
        return keyContent[CONTENT]

def deleteData(KEY):
    dataFile = getSessionData()
    data = plistlib.readPlist(dataFile)

    del data[KEY]
    plistlib.writePlist(data, dataFile)

def modifyData(KEY, CONTENT=None, NEWKEY=None, NEWCONTENT=None):
    # Import dicts
    from main import date as d
    dataFile = getSessionData()
    data = plistlib.readPlist(dataFile)

    if NEWKEY is None:
        keyData = data[KEY]
        keyData[CONTENT] = NEWCONTENT
        keyData['LastModified'] = d['today_full']
    else:
        data[NEWKEY] = data.pop(KEY)
        keyData = data[NEWKEY]
        keyPath = data[NEWKEY]
        keyPath[CONTENT] = NEWCONTENT
        keyData['LastModified'] = d['today_full']

    plistlib.writePlist(data, dataFile)

def iterateKeys():
    dataFile = getSessionData()
    data = plistlib.readPlist(dataFile)

    keys = []
    for key in data:
        keys.append(key)

    return keys