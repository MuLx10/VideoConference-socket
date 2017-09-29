import socket
from utils import audiosocket
from utils.audiofeed import AudioFeed
import sys
import thread
class Server:
    def __init__(self,host,port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.audiofeed = AudioFeed()
        print "TCP AServer Waiting for client on port "+str(port)

    def socket_handler(self,client_socket):
        asock = audiosocket.audiosocket(client_socket)
        while True:
            data=asock.areceive()
            self.audiofeed.set_data(data)
            data=self.audiofeed.get_data()
            asock.asend(data)
        
    def start(self,port):
    	print "Starting Audio Server  : "+str(port)
        while 1:
            client_socket, address = self.server_socket.accept()
            print "I got a connection from ", address
            thread.start_new_thread(self.socket_handler, (client_socket,))

if __name__ == "__main__":
    ip_addr = "127.0.0.1"
    port = 6000
    if len(sys.argv) > 2:
        ip_addr = sys.argv[1]
        port = int(sys.argv[2])

    server = Server(ip_addr,port)
    server.start(port)
