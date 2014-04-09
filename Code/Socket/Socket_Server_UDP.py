import socket

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
while True:
    #wait for a msg
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("received message:", data)
    print ("time : ",cnt)
    cnt += 1
    print("sending msg")
    send_msg(cnt,addr)

    
print ("end server")