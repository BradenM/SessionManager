# Program: Session Manager
# File: utils/process.py
# Desc: Process Images and AppleScript
# Author: Braden Mars

import subprocess


# AppleScript
def applescript(ascript):

    osa = subprocess.Popen(['osascript', '-'],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
    stdout, stderr = osa.communicate(ascript)
    return osa.returncode, stdout, stderr


def asquote(astr):

    astr = astr.replace('"', '" & quote & "')
    return '"{}"'.format(astr)

