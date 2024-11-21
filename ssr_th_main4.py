import threading
import queue
from ssr_sw_class2 import ssr_sw
import RPi.GPIO as GPIO
import random

gpio=[11,12,13,15,16,18]
#
qu=[]
for i in range(0,len(gpio)):
  qu.append(queue.Queue())
th=[]
for i in range(0,len(gpio)):
  th.append("")
for i in range(0,len(gpio)):
  qu[i].put(0)
#
ssrs=[]
for i in range(0,len(gpio)):
  ssrs.append(ssr_sw(gpio[i]))
#
while True:
  try:
    if threading.active_count()==len(gpio)+1:
      continue
    elif threading.active_count()<len(gpio)+1:
      for i in range(0,len(gpio)):
        if qu[i].get()==0:
          t_on=random.randrange(2,5,1)
          t_off=random.randrange(1,5,1)
          th[i]=threading.Thread(target=ssrs[i].run,args=(t_on,t_off,qu[i]),daemon=True)
          th[i].start()
        else:
            continue
    else:
       continue
#
  except KeyboardInterrupt:
    print("Keyboard Interrupt")
    GPIO.cleanup()
    exit()
