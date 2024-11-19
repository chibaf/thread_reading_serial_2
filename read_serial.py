import threading
import queue,time
import serial,sys
from read_serial_sub import read_serial

i=1
q =queue.Queue()  # queue which stores a result of a thread
th = threading.Thread(target=read_serial, args=(sys.argv[1],sys.argv[2],q),daemon=True)
th.start()
print("start thread: "+str(i))
#th.join()
while True:
  if threading.active_count()==1:
    data = q.get()
    print(data)
    i=i+1
    if i>5:
      break;
    th = threading.Thread(target=read_serial, args=(sys.argv[1],sys.argv[2],q),daemon=True)
    th.start()
    print("start thread: "+str(i))

exit()
