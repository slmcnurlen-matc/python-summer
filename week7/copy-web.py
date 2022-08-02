#!/usr/bin/env python3
"""
Sam McNurlen
This script uses modules to copy a webpage.
"""

import requests
response = requests.get("http://notpurple.com")
with open("my_web_file.html", "w") as hFile:
    hFile.write(response.text)