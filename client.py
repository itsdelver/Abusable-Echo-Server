import socket
import sys

target = '127.0.0.1'
port = 6660
msg = str(sys.argv[1])


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target, port))

client.send(msg)
response = client.recv(4096)

print(response)
