#server listens for a request and sends a response
#A single server can run multiple services which can have diffrent port numbers

#This code is for creating the server
import socket
s=socket.socket()#s for server, socket('ipv4/ipv6','tcp/udp')
print('socket created...')

s.bind(('localhost',9999))
s.listen(3)#no. of clients, refuse on 4
print('waiting for connections.....')

while True:
    c,addr=s.accept() #c=client socket, addr=client address
    name=c.recv(1024).decode()
    print("connected with",addr,name)

    c.send(bytes('Welcome to my server....','utf-8'))
    c.close()