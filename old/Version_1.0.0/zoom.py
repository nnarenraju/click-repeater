#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
foo.py
    Short abstract of foo.py
    Additional description

Created on Sat Jul 18 18:41:01 2020

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

import time
import msvcrt
import win32api
import pyautogui

class Simon():
    
    def __init__(self):
        self.flag = None
        self.message = []
    
    def set_flag(self):
        """
        Click on any key to set it as your quit flag
        Stores the key as a bit value
        
        """
        print("Set a quit flag...")
        while True:
            if msvcrt.kbhit():
                self.flag = msvcrt.getch()
                print("Key captured.")
                break    
    
    def _play_(self, interval=2):
        for foo in self.message:
            pyautogui.moveTo(foo[0], foo[1], 0.1)
            pyautogui.click(x=foo[0], y=foo[1], button='left', interval=interval)
        
    def record(self):
        print("Waiting for flag...")
        while True:
            if msvcrt.kbhit():
                if msvcrt.getch() == self.flag:
                    print("Key confirmed.")
                    break
        
        print("Recording started...")
        # Left button down = 0 or 1. Button up = -127 or -128
        state_left = win32api.GetKeyState(0x01)
        message = []
        while True:
            # If flag is clicked again, recording stops
            if msvcrt.kbhit():
                if msvcrt.getch() == self.flag:
                    break
            
            # Resetting left mouse click state
            click = win32api.GetKeyState(0x01)

            if click != state_left:  # Button state changed
                state_left = click
                if click < 0:
                    print('Left Button Pressed')
                    # Get the mouse coordinates
                    x, y = pyautogui.position()
                    x = float(x)
                    y = float(y)
                    message.append([x,y])
                else:
                    print('Left Button Released')
        
        self.message = message
        print("Message has been recorded!")
        print("Replaying message in 5 seconds...")
        time.sleep(5)
        self._play_(interval=2)
        print("Recording successful!")
    
    def repeat(self, nrepeat=1, interval=3):
        ncycle = 1
        while ncycle <=nrepeat:
            self._play_(interval=interval)
            ncycle+=1
        print("Cycles completed!")
        
if __name__ == '__main__':
    s = Simon()
    s.set_flag()
    s.record()
    print("Repeat mode starts in 30 seconds...")
    time.sleep(30)
    print("Repeat mode starting")
    s.repeat(nrepeat=5, interval=2)
    print("End")
    
    
    
    
    
    