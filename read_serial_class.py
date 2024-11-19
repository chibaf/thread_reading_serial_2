import numpy as np
import serial,time

def read_serial(port,speed,q):
  ser=serial.Serial(port,speed)  #open serial port
  time.sleep(1)
  line = ser.readline()
  data=line.strip().decode('utf-8',errors='replace')
  ser.close()
  q.put(data)
  return