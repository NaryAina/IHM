import socket
import time
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "4.2" #envoyer un nombre qui devra etre traite

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
                     
#for i in range(0,100):
while True :
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    time.sleep(0.1)

