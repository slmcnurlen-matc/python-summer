#!/usr/bin/env python3
"""
Sam McNurlen
This script uses the json module to translate JSON into a Python dictionary.
"""

import json,requests,argparse
parser = argparse.ArgumentParser(description='Creating a parser to add arguments')
parser.add_argument('--ipaddress', dest='varIP')
ip = parser.parse_args().varIP
myJSON = requests.get(f"https://ipinfo.io/{ip}/json")
myDict = json.loads(myJSON.text)
for key in myDict:
    print(f"{key} : {myDict[key]}")