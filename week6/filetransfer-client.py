#!/usr/bin/env python3
"""
Sam McNurlen
This script opens a file and sends it to the server.
"""

import socket

with open("file.txt", "r") as hFile:
    SND_DATA = hFile.read()

RHOST = '127.0.0.1'
RPORT = 5000
RCV_DATA = ""

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    C_SOCK.connect((RHOST,RPORT))
    C_SOCK.send(bytearray(SND_DATA, 'utf8'))
    RCV_DATA = C_SOCK.recv(1024)
    print(RCV_DATA.decode())
except socket.error as e:
    print(f"Connection State: {RPORT}::{e}")
C_SOCK.close()