# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Foobar.py
    Description of Foobar

Created on Thu Jul 30 18:20:12 2020

__author__      = nnarenraju
__copyright__   = Copyright 2020, ProjectName
__credits__     = "nnarenraju"
__license__     = Apache License 2.0
__version__     = 1.0.0
__maintainer__  = nnarenraju
__email__       = nnarenraju@gmail.com
__status__      = ['inProgress', 'Archived', 'inUsage', 'Debugging']


Github Repository: NULL

Documentation: NULL

"""

from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press) as listener:
    listener.join()