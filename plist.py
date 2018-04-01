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

def getDataFile():
    from main import paths as p
    global dataFile
    dataFile = os.path.expanduser(p['data'])
    return dataFile

def createList():
    dataFile = getDataFile()
    plistlib.writePlist(pl, dataFile)


def addData(SESSIONNAME, PATH, PHOTOCOUNT, DESC, RAWSTAT):
    # Imports Dictionaries
    from main import date as d
    dataFile = getDataFile()

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

    oldList = plistlib.readPlist(dataFile)
    newList = {}
    newList.update(oldList.items())
    newList.update(Session.items())
    plistlib.writePlist(newList, dataFile)

def validateKey(KEY):
    dataFile = getDataFile()
    data = plistlib.readPlist(dataFile)

    if KEY in data:
        return(True)
    else:
        return(False)

def retrieveData(KEY, CONTENT=None):
    dataFile = getDataFile()
    data = plistlib.readPlist(dataFile)

    keyContent = data[KEY]
    if CONTENT is None:
        return data[KEY]
    else:
        return keyContent[CONTENT]

def deleteData(KEY):
    dataFile = getDataFile()
    data = plistlib.readPlist(dataFile)

    del data[KEY]
    plistlib.writePlist(data, dataFile)

def modifyData(KEY, CONTENT=None, NEWKEY=None, NEWCONTENT=None):
    # Import dicts
    from main import date as d
    dataFile = getDataFile()
    data = plistlib.readPlist(dataFile)

    if NEWKEY == None:
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
    dataFile = getDataFile()
    data = plistlib.readPlist(dataFile)

    keys = []
    for key in data:
        keys.append(key)

    return keys