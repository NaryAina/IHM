import socket
import time
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
cnt = 0

def send_msg(msg,addr):
    MESSAGE = bytes(str(cnt))
    sock.sendto(MESSAGE, addr)
    print "msg send"

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

print ("Serveur online")
data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

while True:
    #wait for a msg
    
    #print ("received message:", data)
    cnt += 1
    print("sending msg : ", cnt)
    send_msg(cnt,addr)
    time.sleep(1)
    
print ("end server")