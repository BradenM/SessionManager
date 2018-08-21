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
