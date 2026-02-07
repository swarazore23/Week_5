from machine import Pin
import time
import neopixel

my_np = neopixel.NeoPixel(Pin(14),16)

while True:
    for n in range(0,16,1):
        my_np[n] = (0,0,50)
        my_np.write()
        time.sleep(0.5)
        print(my_np)
    for n in range (0,16,1):
        my_np[n]=(0,0,0)
        my_np.write()



    