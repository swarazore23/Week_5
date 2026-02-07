from machine import Pin
import time
import neopixel

#make an object for the neopixel
my_np = neopixel.NeoPixel(Pin(14),16)
#16= NUMBER OF led on neopixel
#led = Pin(32, Pin.OUT)
my_np[1]=(255,0,0)#1ST led is red colour
my_np[2]=(0,0,255)
my_np[3]=(0,255,0)
my_np.write()
