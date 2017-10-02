from src import clientA
from src import clientV
import thread
from multiprocessing import Process


import sys

ip_addr = "127.0.0.1"

portA = 6000

if len(sys.argv)>2:
	ip_addr = sys.argv[1]
	portA = int(sys.argv[2])


portV = portA+1





clientA = clientA.Client(ip_addr,portA)
clientV = clientV.Client(ip_addr,portV)

# thread.start_new_thread(clientA.connect,())
# thread.start_new_thread(clientV.connect,())

# clientV.connect(portV)
# clientA.connect()


# p = Process(target=clientA.connect, args=(portA,))
# p.start()

p = Process(target=clientV.connect, args=(portV,))
p.start()
