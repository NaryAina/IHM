import socket
    
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

limitMsg = 5
MsgCnt = 0
#while MsgCnt < limitMsg:
Online = True
#print("Serveur blender online")
#sock.setblocking(0)


data = ''
try:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("ok")
except:
    pass

if data != '':
    MsgCnt += 1
    print ("received message:", data)

#convert data (binary) to string
#dataString = data.decode("ascii")
#dataFloat = float(dataString)

#test on print
#print("data + 10 = ", str(dataFloat+10))
sock.close()
#print("Serveur blender offline")

from bge import logic as gl
gl.truc=42
    
#print(gl.GlobalDict["truc"])