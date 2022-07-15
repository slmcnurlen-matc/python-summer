#!/usr/bin/env python3
print("Name: Sam McNUrlen")
"""
Sam McNurlen
This script takes words from a text file and combines them into a string.
"""

with open("slicing-file.txt", "r") as hFile:
    hFile = hFile.readlines()
a = hFile[24:25]
b = hFile[2:5]
c = hFile[17:12:-2]
d = hFile[10:13]
e = hFile[8:5:-1]
quote = " ".join(a)
b = "".join(b)
c = "".join(c)
d = "".join(d)
e = "".join(e)
quote = quote + b + c + d + e
quote = quote.replace('\n', ' ')
print(quote)