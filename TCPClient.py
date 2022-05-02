import socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '349.168.1.104'
host = socket.gethostname()
port = 444

clientsocket.connect(('349.02.3.23', 6677))

message = clientsocket.recv(1024)
clientsocket.close()
print(message.decode('ascii'))
