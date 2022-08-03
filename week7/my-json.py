#!/usr/bin/env python3
"""
Sam McNurlen
This script uses the json module to translate JSON into a Python dictionary.
"""

import json,requests,argparse
parser = argparse.ArgumentParser(description='Creating a parser to add arguments')
parser.add_argument('--ipaddress')
myJSON = requests.get("https://ipinfo.io/52.54.31.231/json")
myDict = json.loads(myJSON.text)
for key in myDict:
    print(f"{key} : {myDict[key]}")