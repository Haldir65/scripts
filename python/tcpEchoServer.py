import socket as socket

import sys
import os
import signal


def signal_handler(signal, frame):
    print('receving signal , exiting !')
    os._exit(0)

PORT = 13131
signal.signal(signal.SIGINT, signal_handler)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
s.bind(('127.0.0.1',PORT))
s.listen(100)
print('accepting connection on port {0}'.format(PORT))

while True:
    conn, addr = s.accept()
    print("'Connected by', {0}".format(addr))
    while True:
        data = conn.recv(1024)
        if data:
            conn.sendall(data)
            print("send back {0}", data)
            break
        else:
            break
