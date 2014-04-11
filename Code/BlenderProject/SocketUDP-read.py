import socket
from bge import logic as gl

data = ''
try:
    data, addr = gl.sock.recvfrom(1024) # buffer size is 1024 bytes
    print("ok")
except:
    pass
