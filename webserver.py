import socket
import sys

s = socket.socket()
port = 27333
if len(sys.argv) >= 2:
    port = int(sys.argv[1])
connection = ('', port)
s.bind(connection)
s.listen()
while True:
    new_conn = s.accept()
    print(new_conn)
    new_socket = new_conn[0]

    data = "aa"
    while data != '\r\n\r\n':
        data = new_socket.recv(40)
        if data != '\r\n\r\n':
            data = data.decode()
            print(data, end="")

    message = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\n\r\nHello!"""
    new_socket.sendall(message.encode())
    new_socket.close()