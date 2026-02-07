from machine import Pin
import time
import neopixel

my_np = neopixel.NeoPixel(Pin(14),16)

while True:
    my_np[0]=(0,50,0)
    my_np.write()
    time.sleep(0.5)

    my_np[1]=(50,0,0)
    my_np.write()
    time.sleep(0.5)
    #1ST led is red colour
    my_np[2]=(0,0,50)
    my_np.write()
    time.sleep(0.5)

    my_np[3]=(0,50,0)
    my_np.write()
    time.sleep(0.5)

    my_np[4]=(50,0,0)
    my_np.write()
    time.sleep(0.5)

    my_np[5]=(50,0,0)
    my_np.write()
    time.sleep(0.5)
    #1ST led is red colour
    my_np[6]=(0,0,50)
    my_np.write()
    time.sleep(0.5)

    my_np[7]=(0,50,0)
    my_np.write()
    time.sleep(0.5)

    my_np[8]=(50,0,0)
    my_np.write()
    time.sleep(0.5)
    #1ST led is red colour
    my_np[9]=(0,0,50)
    my_np.write()
    time.sleep(0.5)

    my_np[10]=(0,50,0)
    my_np.write()
    time.sleep(1)

    my_np[11]=(50,0,0)
    my_np.write()
    time.sleep(0.5)
    #1ST led is red colour
    my_np[12]=(0,0,50)
    my_np.write()
    time.sleep(0.5)

    my_np[13]=(0,50,0)
    my_np.write()
    time.sleep(0.5)

    my_np[14]=(50,0,0)
    my_np.write()
    time.sleep(0.5)
    #1ST led is red colour
    my_np[15]=(0,0,50)
    my_np.write()
    time.sleep(0.5)
    
    my_np[0] = (0,0,0)
    my_np.write()
    time.sleep(0.5)

