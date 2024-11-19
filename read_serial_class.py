class read_serial():

  def read(self,ser,q):
    import serial,time
    time.sleep(1)
    line=ser.readline()
    data=line.strip().decode('utf-8',errors='replace')
    q.put(data)
    return

  def close(self,ser):
    ser.close()
    return