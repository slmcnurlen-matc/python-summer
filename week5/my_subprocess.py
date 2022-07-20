#!/usr/bin/env python3
"""
Sam McNurlen
This script retrieves a list of processes from the system to work with.
"""

import subprocess

CompleatedProcess = subprocess.run(['ps', '-axco', 'command'],stdout=subprocess.PIPE)
myProc = CompleatedProcess
myProcString = myProc.stdout.decode()
myProcList = myProc.stdout.decode().split('\n')
for process in myProcList:
    print(process)
myProcList = myProcList[1:]
print(len(myProcList))