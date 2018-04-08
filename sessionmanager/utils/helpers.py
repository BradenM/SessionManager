# Program: Session Manager
# File: helpers.py
# Desc: Helper functions
# Author: Braden Mars


import time


# Get Date (MonthYear)
def get_month_year():
    date = "%s%s" % (time.strftime("%B"), time.strftime("%Y"))
    return date


# Remove Whitespace
def remove_whitespace(string):
    new_str = string.replace(' ', '')
    return new_str

# Convert Array to string
def data_to_string(data):
    string = ''.join(data[0])
    return string