class read_serial():

  def __init__(self,port,speed):
    import serial
    self.ser=serial.Serial(port,speed)  #open serial port

  def read(self,q):
    import serial,time
    time.sleep(1)
    line = self.ser.readline()
    data=line.strip().decode('utf-8',errors='replace')
    q.put(data)
    return

  def close(self):
    self.ser.close()
    return