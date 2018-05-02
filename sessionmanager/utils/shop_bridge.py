# Program: Session Manager
# File: utils/shop_bridge.py
# Desc: Deal with photoshop
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


def as_quote(astr):

    astr = astr.replace('"', '" & quote & "')
    return '"{}"'.format(astr)


# Open Image in Photoshop
def ps_open(path):
    script = '''
    tell application "Adobe Photoshop CC 2018"
    set filePath to "{fp}"
    open alias filePath as Camera RAW
    end tell'''.format(fp=path)
    applescript(script)
