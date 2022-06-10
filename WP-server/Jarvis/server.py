from re import S
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(20)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("ID:0001-1,MODE:Normal", 'utf-8'))
    clientsocket.close()
