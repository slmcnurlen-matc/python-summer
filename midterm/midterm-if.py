#!/usr/bin/env python3
print("Name: Sam McNurlen")
"""
Sam McNurlen
This script looks through a text file for specific phrases, then adds the numbers of the lines where the phrases were found together.
"""
Total = 0
hFile = open("Midterm-if.txt", "r")
line = hFile.read(10)
while line:
    Total += 1
    if "gmeach18@ed.gov" in line:
        Total += int(Total)
    elif "248.253.63.149" in line:
        Total += int(Total)
    elif "Whiteland" in line:
        Total += int(Total)
    elif "80.222.19.190" in line:
        Total += int(Total)
    elif "Kayley" in line:
        Total += int(Total)
    elif "dcassyqw@microsoft.com" in line:
        Total += int(Total)
    line = hFile.readline()
print(f"The total is: {Total}")
hFile.close()