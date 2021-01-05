# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import re
import time
import shutil
import numpy as np
import urllib.request
import xml.dom.minidom as md
from subprocess import Popen, PIPE

def run(command, out=False):
    process = Popen(command,shell=True,stdout=PIPE,stderr=PIPE)    
    # Get stdout and break
    if out:
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr

# Get the abspath of Zoom.exe
while True:
    stdout,_= run("wmic process where \"name='Zoom.exe'\" get ExecutablePath", out=True)
    if not _:
        PATH = re.search(r'(.:\\.*?\.[\w:]+)', stdout)
        try: foo = PATH.group()
        except: continue
        break

# Save zoom path
path = PATH.group()[:-8]
while True:
    if os.path.exists("SebClientSettings.seb"):
        file = md.parse("SebClientSettings.seb")
        value = file.getElementsByTagName("string")[28].childNodes[0].nodeValue
        file.getElementsByTagName("string")[28].childNodes[0].nodeValue = path
        with open("SebClientSettings.seb", "w") as foo:  
            foo.write(file.toxml())
        break

# Download SEB from SourceForge
url = 'https://sourceforge.net/projects/seb/files/latest/download'
urllib.request.urlretrieve(url, "SEB.exe")
os.startfile("SEB.exe")
stdout,_=run("wmic process where \"name='SEB.exe'\" get ProcessId", out=True)
PID_seb  = re.findall(r'[0-9]+', stdout)

# Locate for .seb savefile location
root,_=run("cd", out=True)
sebsave = root[:-10] + r"\AppData\Roaming\SafeExamBrowser"

flag = 0
parent = "C:\Program Files\SafeExamBrowser\Configuration"
while True:
    # Sanity check for seb.exe finish installation
    if not flag: 
        stdout,_=run("wmic process where \"name='SEB.exe'\" get ProcessId", out=True)
        new = re.findall(r'[0-9]+', stdout)
        diff = np.setdiff1d(np.array(new), np.array(PID_seb))
        if any(diff):
            flag = 1
    # Initialise App Roaming dir
    if os.path.isdir(parent) and flag==1:
        os.startfile(parent+"\SEBConfigTool.exe")
        time.sleep(5)
        run(r"taskkill /IM SEBConfigTool.exe")
        flag = 2
    if os.path.isdir(sebsave):
        shutil.move(r"SebClientSettings.seb", sebsave)
        break
    
    
    
    
    