from datetime import datetime
import socket

#server @ and prot
address = ('localhost',6789)
#max size of sent data
max_size = 1000

print('Starting the server at', datetime.now())
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
#server.listen(5) is configured to queue up to five client connections before refusing new ones
server.listen(5)

#server.accept() gets the first available message as it arrives
client, addr = server.accept()
#client.recv(1000) sets a maximum acceptable message length of 1,000 bytes
data = client.recv(max_size)

print('At', datetime.now(), client, 'said', data)
#sending
client.sendall(b'Are you talking to me?')
#closing client connection
client.close()
#closing server connection
server.close()
