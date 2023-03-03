#SERVER
import socket

host = "localhost"
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)
c, add = s.accept()

print(str(add))

c.send(b"Hello how are you")
msg = "I am fine."
c.send(msg.encode())
c.close()

#CLIENT
import socket

host = "localhost"
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))
msg = s.recv(1024)
# s.recv must have a multiple of 1024
while msg:
    print("Recvd message "+msg.decode())
    msg=s.recv(1024)

s.close()
