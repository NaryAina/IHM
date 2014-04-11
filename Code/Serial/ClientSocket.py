import socket

class ClientSocket :
    def __init__(self, ip, port) :
        self.ip = ip
        self.port = port
        #connect
        self.sock = = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    
    def envoyerMsg(self, msg) :
        self.sock.sendto(msg, (self.ip, self.port))