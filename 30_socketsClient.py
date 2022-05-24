#This code is for creating the client
import socket

c=socket.socket()#c for client, socket('ipv4/ipv6','tcp/udp')

c.connect(('localhost',9999))

name=input("Enter name:")
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())#1024=buffersize