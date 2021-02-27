import socket

HOST = 'localhost'
PORT = 25213

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send("I am CLIENT<br>".encode())
from_server = client.recv(1024)
client.close()

print(from_server)
