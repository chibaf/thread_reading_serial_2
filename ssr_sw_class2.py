class ssr_sw:

  def __init__(self,ssr_pin):
    self.ssr_pin = ssr_pin;  
    import RPi.GPIO as GPIO
    self.pin_id=str(ssr_pin)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ssr_pin,GPIO.OUT)
    
  def run(self,ton,tstop,q):
    import RPi.GPIO as GPIO
    import os
    import time
    q.put(1)
    GPIO.output(self.ssr_pin, 1)
    print("SSR "+self.pin_id+" ON ("+str(ton)+"sec)\n")
    time.sleep(int(ton))
    GPIO.output(self.ssr_pin, 0)
    print("SSR "+self.pin_id+" OFF ("+str(tstop)+"sec)\n")
    time.sleep(int(tstop))
    q.put(0)
    return 
