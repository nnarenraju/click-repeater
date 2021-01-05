# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Foobar.py
    Description of Foobar

Created on Thu Jul 30 18:37:52 2020

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
import keyboard

shot_pressed = 0
was_pressed = False
        
while True:
    if keyboard.is_pressed('s'):
        if not was_pressed:
            shot_pressed += 1
            if shot_pressed == 1:
                print("hello")
            if shot_pressed == 2:
                break
            was_pressed = True
    else:
        was_pressed = False