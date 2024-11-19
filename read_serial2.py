import threading
import queue,time
import serial,sys
from read_serial_class import read_serial

i=0
ser=serial.Serial(sys.argv[1],sys.argv[2])
read_ser=read_serial()
q =queue.Queue()  # queue which stores a result of a thread
th = threading.Thread(target=read_ser.read, args=(ser,q),daemon=True)
th.start()
print("start thread: "+str(i))
while True:
  try:
    if threading.active_count()==1:
      data = q.get()
      print(data)
      i=i+1
      th = threading.Thread(target=read_ser.read, args=(ser,q),daemon=True)
      th.start()
      print("start thread: "+str(i))
  except KeyboardInterrupt:
    print("Keyboard Interrupt")
    read_ser.close(ser)
    exit()
exit()
