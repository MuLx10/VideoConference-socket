from src import serverA
from src import serverV
import thread
from multiprocessing import Process

ip_addr = "127.0.0.1"

portA = 6000
portV = 6001






serverA = serverA.Server(ip_addr,portA)
serverV = serverV.Server(ip_addr,portV)


# serverA.start(portA)

# serverV.start(portV)

p1 = Process(target=serverV.start, args=(portV,))
p1.start()

# p2 = Process(target=serverA.start, args=(portA,))
# p2.start()

# p1.join()
# p2.join()

# thread.start_new_thread(start,(portA,))
# # thread.start_new_thread(serverV.start,(portV,))
# print "new"