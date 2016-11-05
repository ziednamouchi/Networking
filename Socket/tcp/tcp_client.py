import socket
from datetime import datetime

#client @ and port
address = ('localhost', 6789)
#max size of data
max_size = 1000

print('Starting the client at', datetime.now())
#creation of the socket with socket.socket
#creation of IP socket with socket.AF_INET
#send and receive TCP with socket.SOCK_STREAM
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#establishing connection
client.connect(address)
#sending
client.sendall(b'hey!')
#receiving
data = client.recv(max_size)
print('At', datetime.now(), 'someone replied', data)
#closing connection
client.close()
