# echo_server.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 9999))
print("UDP echo server on 9999...")
while True:
    data, addr = s.recvfrom(2048)
    print("got", data, "from", addr)
    s.sendto(b"pong:" + data, addr)
