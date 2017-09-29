import socket
from utils import audiosocket
from utils.audiofeed import AudioFeed
import sys
# import StringIO


class Client:
    def __init__(self, ip_addr = "127.0.0.1",port = 6262):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((ip_addr, port))
        self.asock = audiosocket.audiosocket (self.client_socket)
        self.audiofeed = AudioFeed()
        # self.data = StringIO.StringIO()

    def connect(self,port):
    	print("Client Audio")
        while True:
            data=self.audiofeed.get_data()
            self.asock.asend(data)
            data = self.asock.areceive()
            self.audiofeed.set_data(data)

if __name__ == "__main__":
    ip_addr = "127.0.0.1"
    port = 6000
    if len(sys.argv) == 2:
        ip_addr = sys.argv[1]
        port = int(sys.argv[2])

    print "Connecting to " + ip_addr + "...."+str(port)+'.....'
    client = Client(ip_addr,port)
    client.connect(port)
