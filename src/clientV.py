import socket
from utils import videosocket
from utils.videofeed import VideoFeed
import sys
# import StringIO


class Client:
    def __init__(self, ip_addr = "127.0.0.1",port = 6262):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((ip_addr, port))
        self.vsock = videosocket.videosocket (self.client_socket)
        self.videofeed = VideoFeed(1,"client",-1)

    def connect(self,port):
        print("Client Video")
        while True:
            # frame=self.videofeed.get_frame()
            # self.vsock.vsend(frame)
            frame = self.vsock.vreceive()
            self.videofeed.set_frame(frame)

if __name__ == "__main__":
    ip_addr = "127.0.0.1"
    port = 6001
    if len(sys.argv) > 2:
        ip_addr = sys.argv[1]
        port = int(sys.argv[2])

    print "Connecting to " + ip_addr + "...."+str(port)+'.....'
    client = Client(ip_addr,port)
    client.connect(port)
