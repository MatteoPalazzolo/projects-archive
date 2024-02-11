import socket

s = socket.socket()
s.connect(('socket.cryptohack.org', 11112))
print(f"LOG: server connection established")
    
request = s.recv(4096)
print(request)