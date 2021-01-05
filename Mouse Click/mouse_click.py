#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
foo.py
    Short abstract of foo.py
    Additional description

Created on Sat Jul 18 20:04:03 2020

__author__      = nnarenraju
__copyright__   = Copyright 2020, Project Name
__credits__     = nnarenraju
__license__     = Apache License 2.0
__version__     = 1.0.0
__maintainer__  = nnarenraju
__email__       = nnarenraju@gmail.com
__status__      = ['inProgress', 'inUsage', 'Archived', 'Debugging']


Github Repository: NULL

Documentation: NULL

"""


# Code to check if left or right mouse buttons were pressed
import win32api
import time

state_left = win32api.GetKeyState(0x01)

while True:
    a = win32api.GetKeyState(0x01)

    if a != state_left:  # Button state changed
        state_left = a
        if a < 0:
            print('Left Button Pressed')
        else:
            print('Left Button Released')
    time.sleep(0.001)