#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simon.py
    Repeats mouse clicks with provided intervals
    Verbosity is currently not togglable and is set to 1

Created on Sat Jul 18 18:41:01 2020

__author__      = nnarenraju
__copyright__   = Copyright 2020, Simon Says
__credits__     = nnarenraju
__license__     = Apache License 2.0
__version__     = 1.0.0
__maintainer__  = nnarenraju
__email__       = nnarenraju@gmail.com
__status__      = inUsage


Github Repository: NULL

Documentation: README.md provided alongside package

"""

import time
import keyboard
import win32api
import pyautogui

class Simon():
    
    def __init__(self):
        self.flag = None
        self.message = []
        self.intervals = []
    
    def set_flag(self):
        """
        Click on any key to set it as your quit flag
        Stores the key as a bit value
        
        """
        print("Set a quit flag...")
        self.flag = input("Enter a flag:\t")
        print("Key captured.")
    
    def _play_(self, interval=[]):
        if not interval:
            interval = [2]*len(self.message)
        for m, dt in zip(self.message, interval):
            pyautogui.moveTo(m[0], m[1], 0.1)
            pyautogui.click(x=m[0], y=m[1], button='left', interval=dt)
        
    def record(self):
        print("Waiting for flag...")
        # Left button down = 0 or 1. Button up = -127 or -128
        state_left = win32api.GetKeyState(0x01)
        message = []
        
        shot_pressed = 0
        was_pressed = False
        
        while True:
            if keyboard.is_pressed(self.flag):
                if not was_pressed:
                    shot_pressed += 1
                    if shot_pressed == 1:
                        print("Recording started...")
                    if shot_pressed == 2:
                        # If flag is clicked again, recording stops
                        break
                    was_pressed = True
            else:
                was_pressed = False
            
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
        self._play_()
        print("Recording successful!")
    
    def repeat(self, nrepeat, interval):
        ncycle = 1
        while ncycle <=nrepeat:
            self._play_(interval=interval)
            ncycle+=1
        print("Cycles completed!")
        
if __name__ == '__main__':
    s = Simon()
    s.set_flag()
    s.record()
    
    # Get the interval from user
    for n,_ in enumerate(s.message[:-1]):
        print("\nInterval between click index {0} and {1}".format(n, n+1))
        interval = int(input("Enter interval (in seconds):\t"))
        s.intervals.append(interval)
    repdt = int(input("\nEnter interval between repetitions (in seconds):\t"))
    s.intervals.append(repdt)
    
    response = input("\nStart repeat mode (y or n)?\t")
    if response=='y' or response=='Y':
        print("Number of repeats can be any integer (set as -1 to repeat indefinitely)")
        nrep = int(input("Enter the number of repeats: "))
        if nrep==-1:
            nrep=999999
        print("\nRepeat mode starts in 30 seconds...")
        time.sleep(30)
        print("Repeat mode starting")
        s.repeat(nrepeat=nrep, interval=s.intervals)
    print("End")
    
    