#!/usr/bin/env python3
"""
Sam McNurlen
This script uses modules to get a list of links from a webpage.
"""

import requests, bs4
res = requests.get('http://notpurple.com')
try:
    res.raise_for_status()
    myHTML = bs4.BeautifulSoup(res.text, features='html.parser')
    print(myHTML.title.text)
    for link in myHTML.find_all("a"):
        print("Links : " + link.text)
except Exception as e:
    print("Something went wrong. Error: "+str(e))