"""
This example shows that python suffers from some problem of
not being able to reuse sockets even though the socket.SO_REUSEADDR
is used...
"""

import socket

while True:
    adr = ('localhost', 8080)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(adr)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(15)
    s.accept()
    s.shutdown(socket.SHUT_RDWR)
