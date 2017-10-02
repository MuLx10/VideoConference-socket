from src import serverA
from src import serverV
import thread
from multiprocessing import Process
import sys

ip_addr = "127.0.0.1"

portA = 6000

if len(sys.argv)>2:
	ip_addr = sys.argv[1]
	portA = int(sys.argv[2])


portV = portA+1




serverA = serverA.Server(ip_addr,portA)
serverV = serverV.Server(ip_addr,portV)


# serverA.start(portA)

# serverV.start(portV)

p1 = Process(target=serverV.start, args=(portV,))
p1.start()

p2 = Process(target=serverA.start, args=(portA,))
p2.start()

# p1.join()
# p2.join()

# thread.start_new_thread(start,(portA,))
# # thread.start_new_thread(serverV.start,(portV,))
# print "new"
