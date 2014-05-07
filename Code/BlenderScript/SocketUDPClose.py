#import socket
from bge import logic as gl

def main() :
    gl.sock.close()
    print("close socket")
    
if __name__ == "__main__":
    main()