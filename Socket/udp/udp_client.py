import socket
from datetime import datetime

server_address = ('localhost',6789)# server @ and port
max_size = 4096#max size of data

print('Starting the client at', datetime.now())
#creating socket with socket.socket
#AF_INET-> creating IP socket
#SOCK_DGRAM->send and receive udp
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sending data
client.sendto(b'hey!', server_address)
#recvfrom-> receiving datagram
data, server = client.recvfrom(max_size)
print('At', datetime.now(), server, 'said', data)
#close connection
client.close()
