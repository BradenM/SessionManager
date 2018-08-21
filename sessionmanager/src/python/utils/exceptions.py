'''
Program: Session Manager
File: utils/exception.py
Desc: Exceptions
Author: Braden Mars
'''


class NoRawFiles(Exception):
    '''
    No Raw Files
    Raised when no .CR2 files are found in a path

    Params:
        path (string): Path to .CR2 Raw images
    '''

    def __init__(self, path):
        error_alias = 'NoRawFiles'
        Exception.__init__(
            self, f'[{error_alias}] No .CR2 Files were found in path: ({path})')


class SessionExists(Exception):
    '''
    Session Exists
    Raised when a new session object is created with an existing one
    sharing it's name

    Params:
        name (string): Name of new session object
    '''

    def __init__(self, name):
        error_alias = 'SessionExists'
        Exception.__init__(
            self, f'[{error_alias}] A Session with the name ({name}) already exists.')
