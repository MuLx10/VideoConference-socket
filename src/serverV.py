import socket
from utils import videosocket
from utils.videofeed import VideoFeed
import sys
import thread

class Server:
    def __init__(self,host,port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.videofeed = VideoFeed(1,"server",1)
        print "TCPServer Waiting for client on port "+str(port)

    def socket_handler(self,client_socket):
        vsock = videosocket.videosocket(client_socket)
        while True:
            frame=vsock.vreceive()
            self.videofeed.set_frame(frame)
            frame=self.videofeed.get_frame()
            vsock.vsend(frame)
    	

    def start(self,port):
        print "Starting Video Server  : "+str(port)
        while 1:
            client_socket, address = self.server_socket.accept()
            print "I got a connection from ", address
            # self.socket_handler(client_socket)
            thread.start_new_thread(self.socket_handler, (client_socket,))



if __name__ == "__main__":
    ip_addr = "127.0.0.1"
    port = 6260
    if len(sys.argv) > 2:
        ip_addr = sys.argv[1]
        port = int(sys.argv[2])
    server = Server(ip_addr,port)
    server.start(port)
