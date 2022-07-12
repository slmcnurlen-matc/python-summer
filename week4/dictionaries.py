#!/usr/bin/env python3
"""
Sam McNurlen
This script demonstrates how to use dictionaries in Python.
"""

servers = {}
servers['server1.testlab.com'] = '192.168.1.10'
servers['server2.testlab.com'] = '192.168.1.11'
servers['server3.testlab.com'] = '192.168.1.12'
servers['server4.testlab.com'] = '192.168.1.13'
servers['server5.testlab.com'] = '192.168.1.14'
servers['server6.testlab.com'] = '192.168.1.15'

print(servers.keys())
print(servers.values())
print(servers.items())

servers['server7.testlab.com'] = '192.168.1.16'
servers['server8.testlab.com'] = '192.168.1.17'

print('server2.testlab.com' in servers)
print('server10.testlab.com' in servers)