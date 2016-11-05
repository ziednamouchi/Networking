#first program
from datetime import datetime
import socket

server_address = ('localhost', 6789)# server @ and port
max_size = 4096 #max size of data
print('Starting the server at', datetime.now())
print('Waiting for a client to call.')
#creating socket with socket.socket
#AF_INET-> creating IP socket
#SOCK_DGRAM->send and receive udp
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)
#recvfrom-> receiving datagram
data, client = server.recvfrom(max_size)
print('At', datetime.now(), client, 'said', data)
#sending data
server.sendto(b'Are talking to me?', client)
#close connection
server.close()
