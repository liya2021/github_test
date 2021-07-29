import sys

import socket

sys.setdefaultemcoding('utf-8')

socket.socket('socket.AF_af_IOONT',socket.sock_STREAM)

server.bind("localhost", '9090')
server.listen(5)
while True:
    conn,addr = server.accept()
    print(conn,addr)
    while True:
        data = conn.recv(1024)
        print('recive',data.decode())
        conn.sebd(data.upper)

conn.close()