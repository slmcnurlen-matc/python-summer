#!/usr/bin/env python3
"""
Sam McNurlen
This script receives a message from the client and echos it back.
"""

import socket

LHOST = ''
LPORT = 5000
RCV_DATA = ""
L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))
while 1:
    L_SOCK.listen(1)
    L_CONN, addr = L_SOCK.accept()
    print('Connected by ', addr)
    while 1:
        RCV_DATA = L_CONN.recv(1024)
        if not RCV_DATA: break
        print(f"The server received this data: {RCV_DATA}")
        L_CONN.sendall(RCV_DATA)
    L_CONN.close()