from src import clientA
from src import clientV
import thread
from multiprocessing import Process


ip_addr = "127.0.0.1"

portA = 6000
portV = 6001






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
