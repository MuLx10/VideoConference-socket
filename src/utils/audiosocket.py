import socket

class audiosocket:
    '''A special type of socket to handle the sending and receiveing of fixed
       size frame strings over ususal sockets
       Size of a packet or whatever is assumed to be less than 100MB
    '''

    def __init__(self , sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock= sock
        self.size = 1024

    def connect(self,host,port):
        self.sock.connect((host,port))

    def asend(self, data):
        self.sock.send(data)

    def areceive(self):
        data = self.sock.recv(self.size)
        return data


   


        
