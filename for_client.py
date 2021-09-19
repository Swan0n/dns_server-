import socket

prox_sock=socket.socket()
prox_sock.connect(('localhost', 8397))
prox_sock.send('gaagl.com'.encode())

data=prox_sock.recv(1024)
prox_sock.close()


print(data.decode())