"""
Echo server program
"""

import socket

HOST = "0.0.0.0"  # this means all interfaces
PORT = 5000  # arbitrary non-privileged port (above 1024, can be listened to by non-root user)
af = socket.AF_INET
socket_type = socket.SOCK_STREAM
proto = socket.IPPROTO_TCP
socket_address = (HOST, PORT)

s = socket.socket(af, socket_type, proto)
s.bind(socket_address)
s.listen(1)
print(f"contact me at {socket_address}")
while True:
    conn, address = s.accept()
    print(f"Connected by {address}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data)
    print("connection closed")
    conn.close()
