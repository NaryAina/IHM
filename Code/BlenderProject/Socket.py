import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

limitMsg = 5
MsgCnt = 0
while MsgCnt < limitMsg:
    MsgCnt += 1
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("received message:", data)
    
    #convert data (binary) to string
    dataString = data.decode("ascii")
    dataFloat = float(dataString)
    
    #test on print
    print("data + 10 = ", str(dataFloat+10))
    

    
    
