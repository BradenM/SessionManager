# Program: Session Manager
# File: sessions.py
# Desc: Manages sessions
# Author: Braden Mars

# Imports
import sys
import os
import time
import argparse
from shutil import copyfile, rmtree
import subprocess
import psutil
# Files
import plist
import signal


# Create Session
def createSession():

    # Import Dictionaries
    from main import paths as p, argData as a, date as d

    # Check PATH
    if os.path.isdir(a['path']):
        imageDir = os.listdir(a['path'])
    else:
        print("Image path is invalid.")
        exit()

    # Check Parent folder (Date)
    parfolderName = "%s%s" % (d['month'], d['year'])
    if os.path.isdir("%s/%s" % (p['main'], parfolderName)):
        print("Folder for date: %s , exist. Continuing." % parfolderName)
    else:
        print("Folder for date: %s , does not exist. Creating..." % parfolderName)
        os.mkdir("%s/%s" % (p['main'], parfolderName))


    # Create Session folder tree
    newSesDir = "%s/%s/%s" % (p['main'], parfolderName, a['name'].replace(' ', ''))
    fullnewSesDir = "%s/%s" % (p['cwd'], newSesDir)
    try:
        os.mkdir(newSesDir)
        os.mkdir("%s/RAW" % newSesDir)
    except:
        print("You already have a session named '%s'. Please create one with a different name" % a['name'])
        exit()
    print("Session file tree setup, moving images...")


    # Find and copy RAW files in path given.
    cr2 = []
    for file in imageDir:
        if file.endswith(".CR2"):
            copyfile("%s/%s" % (a['path'], file), "%s/RAW/%s" % (newSesDir, file))
            cr2.append(file)

    # Convert RAW to DNG
    #os.system("open -a %s --args -p2 %s/%s/RAW/*.CR2" % (p['dng'], p['cwd'], newSesDir))
    subprocess.Popen("open -a %s --args -p2 %s/%s/RAW/*.CR2" % (p['dng'], p['cwd'], newSesDir), shell=True)
        # Wait for DNG converter to finish
    dng = []
    while True:
        for file in os.listdir("%s/RAW/" % newSesDir):
            if file.endswith(".dng"):
                dng.append(file)
        if len(dng) >= len(cr2):
            time.sleep(1)
            print("Finished converting")
            break
        else:
            print("Converting...(%s/%s)" %(len(dng), len(cr2)))
            dng = []
            time.sleep(2)

    # Move DNG files up one directory
    os.system("mv %s/RAW/*.dng %s" % (newSesDir, newSesDir))


    # Delete RAW files unless -kr argument is passed
    if a['keepraw'] != True:
        rmtree("%s/RAW" % newSesDir)
        print("RAW Files deleted.")
    else:
        print("-r argument passed, RAW files kept.")

    # Create PLIST entry
    plist.addSession(a['name'], fullnewSesDir, len(cr2), a['desc'], a['keepraw'])
    print("Info for session '%s' added to information file." % a['name'])
    # File data PLIST entry
    plist.createDataList(a['name'])
    x = 1
    for file in os.listdir("%s" % newSesDir):
        filename = "%s_%s.dng" % (a['name'].replace(" ", ""), x)
        if file.endswith(".dng"):
            os.rename("%s/%s" %(newSesDir, file), "%s/%s" %(newSesDir, filename))
            name = filename.strip(".dng")
            plist.addfileData(a['name'], name)
            x = x+1

    # Finished creating session
    print("Session %s created with %s images" % (a['name'], len(cr2)))



# Delete Session
def deleteSession():
    # Import Dictionaries
    from main import argData as a

    # Validate and Delete
    if plist.validateKey(a['name']):
        print("Session: '%s' located in database" % a['name'])
        try:
            sessionFiles = plist.retrieveData(a['name'], 'Path')
            rmtree(sessionFiles)
        except:
            print("Session Delete failed, exiting...")
            exit()
        print("Session files deleted")
        plist.deleteData(a['name'])
        print("Session info removed from database")
    else:
        print("Session: '%s' does not exist" % a['name'])

def editSession():
    # Import Dictionaries
    from main import paths as p, argData as a, date as d

    # Validate and Edit
    if plist.validateKey(a['name']):
        print("Session: '%s' located in database" % a['name'])
    else:
        print("Session: '%s' does not exist" % a['name'])
        exit()

    desc = plist.retrieveData(a['name'], "Description")
    path = plist.retrieveData(a['name'], "Path")
    prompt="\n\nCurrent Name: %s\nCurrent Description: %s\n\nWhat would you like to change:\n1) Name\n2) Description\n" % (a['name'], desc)
    print(prompt)
    reply = input("(1/2): ")

    if int(reply) == 1:
        content = "Name"
    elif int(reply) == 2:
        content = "Description"
    else:
        print("Invalid input")

    prompt = '\nWhat would you like to change it to?\n'
    print(prompt)
    newCont = input("New %s: " % content)

    if len(newCont) <= 0:
        print('New %s must contain more than 0 characters' % content)
        exit()

    if content == "Name":
        formatName = a['name'].replace(' ', '')
        Npath = path.replace(formatName, newCont.replace(' ', ''))
        os.rename(path, Npath)
        plist.modifyData(KEY=a['name'], NEWKEY=newCont, CONTENT="Path", NEWCONTENT=Npath)
    else:
        plist.modifyData(KEY=a['name'], CONTENT='Description', NEWCONTENT=newCont)

    print("%s's %s changed to '%s'" % (a['name'], content, newCont))

def iterateSessions():
    # Import Dictionaries
    from main import paths as p, argData as a

    keys = plist.iterateKeys()
    keys.remove('Info')
    return keys




