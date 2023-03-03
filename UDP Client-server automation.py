#SEVER
import socket
import time

host = "localhost"
port = 5000

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
time.sleep(10)

s.sendto(b"hello client", ((host, port)))
msg = "How are you"
s.sendto(msg.encode(), ((host, port)))
s.close()
#CLIENT
import socket

host = "localhost"
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((host, port))
c, addr = s.recvfrom(1024)

try:
    s.settimeout(5)
    while c:
        print("Received Message "+c.decode())
        c,addr=s.recvfrom(1024)
except socket.timeout:
    print("Time over")
s.close()
