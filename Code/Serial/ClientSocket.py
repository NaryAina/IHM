import socket

class ClientSocket :
    def __init__(self, ip, port) :
        self.ip = ip
        self.port = port
        #connect
        self.sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        print "opening socket"
    
    def envoyerMsg(self, msg) :
        try :
            self.sock.sendto(msg, (self.ip, self.port))
            print "sent!"
        except :
            pass