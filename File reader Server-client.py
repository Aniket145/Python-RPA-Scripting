#SERVER
import socket
import time

host = "localhost"
port = 5000
s = socket.socket()
s.bind((host,port))
s.listen(1)

c,addr = s.accept()
print("Connected")
f_name = c.recv(1024)
fn=str(f_name.decode())
try:
    print(fn)
    f=open(fn,"rb")
    content = f.read()
    c.send(content)
    print("Data sent")
    f.close()
except FileNotFoundError:
    c.send("File not found")
c.close()
#CLIENT
import socket
import time


host = 'localhost'
port = 5000

s = socket.socket()
s.connect((host,port))


f_name = input("Enter file name:")
s.send(f_name.encode())

content = s.recv(1024)
msg = str(content)
print(msg)
s.close()
