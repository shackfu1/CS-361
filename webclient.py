import socket
import sys

s = socket.socket()
port = 80
if len(sys.argv) >= 3:
    port = int(sys.argv[2])
dest = (sys.argv[1], port)
s.connect(dest)
http = 'GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n '
s.sendall(http.encode())

data = "aa"
while data != b'':
    data = s.recv(40)
    if data != b'':
        data = data.decode()
        print(data, end="")
s.close()