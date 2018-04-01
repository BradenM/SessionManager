# Program: Session Manager
# File: main.py ; primary file
# Version: Alpha
# Desc: Manages photography sessions
# Author: Braden Mars

# Imports
import os
import time
import argparse
# Files
import plist
import sessions
import gmain

# Argument Parsers
    # Parent Parser
parser = argparse.ArgumentParser(prog='Session Manager', description="Manage photography sessions")
subparsers = parser.add_subparsers(title="Subcommands", dest="subparsers")

    # Create Parser
create_parser = subparsers.add_parser('create', description="Create Session", help="Create Session")
create_parser.add_argument("-kr", "--keep-raw", help="Keep RAW files.", action="store_true")
create_parser.add_argument("path", help="File path to images for a session", type=str)
create_parser.add_argument("name", help="Session name", type=str)
create_parser.add_argument("desc", help="Session description", type=str)

    # Delete Parser
delete_parser = subparsers.add_parser('delete', description="Delete Session", help="Delete Session")
delete_parser.add_argument("-b", "--backup", help="Backup Session", action="store_true")
delete_parser.add_argument("name", help="Session name", type=str)

    # Edit Parser
edit_parser = subparsers.add_parser('edit', description="Edit Session", help="Edit Session")
edit_parser.add_argument("name", help="Session Name", type=str)

    # Iterate Parser
iter_parser = subparsers.add_parser('list', description="Search Sessions", help="List Sessions")

eraw_parser = subparsers.add_parser('exportRaw', description="Export RAW Files", help="Export RAW files")
edit_parser.add_argument("name", help="Session Name", type=str)

args = parser.parse_args()

# Dictionaries
paths = {
    "main" : "sessions",
    "dng" : "/Applications/Adobe\ DNG\ Converter.app/Contents/MacOS/Adobe\ DNG\ Converter",
    "cwd" : os.getcwd(),
    "data" : "sessions/sessions.plist",
}

argData = {}




date = {
    "month" : time.strftime("%B"),
    "year" : time.strftime("%Y"),
    "today_date" : time.strftime("%m-%d-%Y"),
    "today_full" : time.strftime('%A %b %d, %Y at %I:%M%p')
}

def argPoint(GUI=False, PATH=None, NAME=None, DESC=None, RAW=False):
    if GUI:
        argData['path'] = PATH
        argData['name'] = NAME
        argData['desc'] = DESC
        argData['keepraw'] = RAW
    else:
        try:
            argData['path'] = args.path
        except AttributeError:
            pass
        try:
            argData['name'] = args.name
        except AttributeError:
            pass
        try:
            argData['desc'] = args.desc
        except AttributeError:
            pass
        try:
            argData['keepraw'] = args.keep_raw
        except AttributeError:
            pass

def main():

    # File Tree Check
    if os.path.isdir(paths['main']):
        print("Sessions directory found. Continuing...")
    else:
        print("Sessions directory does not exist, creating...")
        os.mkdir(paths['main'])
        print("Sessions directory created.")

    # PList Check
    if os.path.isfile(paths["data"]):
        print("Information File found.")
    else:
        plist.createList()
        print("Information file not found, created a new one.")


    # Argument Pointer
    if args.subparsers == "create":
        sessions.createSession()
    elif args.subparsers == "delete":
        sessions.deleteSession()
    elif args.subparsers == "edit":
        sessions.editSession()
    elif args.subparsers == "search":
        sessions.iterateSessions()
    else:
        gmain.start()


def create(PATH, NAME, DESC, RAW):
    if RAW:
        argPoint(True, PATH, NAME, DESC, RAW=True)
    else:
        argPoint(True, PATH, NAME, DESC, RAW=False)

    sessions.createSession()

def delete(NAME):
    argPoint(True, NAME=NAME)
    sessions.deleteSession()


if __name__ == "__main__":
    main()

