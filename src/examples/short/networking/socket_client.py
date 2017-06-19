#!/usr/bin/python3

"""
Echo client program
"""

import socket

HOST = 'localhost'
PORT = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('bla bla bla')
data = s.recv(1024)
s.close()
print('Received', repr(data))
