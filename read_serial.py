import threading
import queue,time
import serial,sys
from read_serial_sub import read_serial

ser=serial.Serial(sys.argv[1],sys.argv[2])
i=1
q =queue.Queue()  # queue which stores a result of a thread
th = threading.Thread(target=read_serial, args=(ser,q),daemon=True)
th.start()
#print("start thread: "+str(i))
#th.join()
#print(ser)
while True:
  try:
    if threading.active_count()==1:
      data = q.get()
      print(data)
      i=i+1
      if i>5:
        break;
      th = threading.Thread(target=read_serial, args=(ser,q),daemon=True)
      th.start()
      print("start thread: "+str(i))
  except KeyboardInterrupt:
    print("key board interrupt occured")
    ser.close()
    exit()
