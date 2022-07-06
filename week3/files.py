#!/usr/bin/env python3
"""
Sam McNurlen
This script demonstrates reading files with Python.
"""
with open("/etc/passwd", "r") as hFile:
    varString = hFile.read()
print(len(varString))
print("The len() function counts the number of characters in the file.")
print("The read() function is used when the user wants to use the whole file at once.")

with open("/etc/passwd", "r") as hFile:
    varList = hFile.readlines()
print(len(varList))
print("The len() function counts the number of items in the list.")
print("The readlines() function is used when the user wants to do something with each line one at a time.")

with open("/etc/passwd", "r") as hFile:
    line = hFile.read()
    while line:
        print(f"{len(line):03d}")
        line = hFile.readline()
print("The readline() function is useful for looping through the file one line at a time.")