import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', sys.argv[0]))
while True:
  data, addr = s.recvfrom(1024)
  print(str(data), addr)
  s.sendto(data, addr)