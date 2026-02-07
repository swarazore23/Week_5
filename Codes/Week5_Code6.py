from machine import Pin
import time
import neopixel

np = neopixel.NeoPixel(Pin(14),16)
pb = Pin(5, Pin.IN, Pin.PULL_UP)
pb2 = Pin(33, Pin.IN, Pin.PULL_UP)
blu = Pin(32, Pin.OUT)

while True:
    con = pb.value()
    print(con)
    lol = pb2.value()
    print(lol)
    if con == 0:
        for n in range (0,16,1):
            np[n] = (0,0,255)
            np.write()
            time.sleep(0.1)
            print(np)
    else:
        for n in range (0,16,1):
            np[n] = (0,0,0)
            np.write()

    if lol == 0:
       blu.on()
       time.sleep(0.2)
    else:
        blu.off()
            
    
   