import threading
import queue,time
import serial
from read_serial_class import read_serial

i=0
ser0=serial.Serial('/dev/ttyACM0',19200)
ser1=serial.Serial('/dev/ttyACM1',19200)
read_ser0=read_serial()
read_ser1=read_serial()
q0=queue.Queue()  # queue which stores a result of a thread
q1=queue.Queue()  # queue which stores a result of a thread
th0=threading.Thread(target=read_ser0.read, args=(ser0,q0),daemon=True)
th0.start()
th1=threading.Thread(target=read_ser1.read, args=(ser1,q1),daemon=True)
th1.start()
print("start thread: "+str(i))
x=range(0, 100, 1)
y0=[0]*100
y1=[0]*100
while True:
  try:
    if threading.active_count()==1:
      y0.pop(-1)
      y1.pop(-1)
      a=q0.get()
      if a[0]=="01":
        y0.insert(0,float(a[1]))
      else: 
        y1.insert(0,float(a[1]))
      a=q1.get()
      if a[0]=="02":
        y1.insert(0,float(a[1]))
      else: 
        y0.insert(0,float(a[1]))
      i=i+1
      th0 = threading.Thread(target=read_ser0.read, args=(ser0,q0),daemon=True)
      th0.start()
      th1 = threading.Thread(target=read_ser1.read, args=(ser1,q1),daemon=True)
      th1.start()
      print("start thread: "+str(i))
  except KeyboardInterrupt:
    print("Keyboard Interrupt")
    read_ser0.close(ser0)
    read_ser1.close(ser1)
    exit()
exit()