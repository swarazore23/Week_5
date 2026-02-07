from machine import Pin,PWM
import time

MY_LED = PWM(Pin(14))

MY_LED.freq(1)
while True:
    for n in range(0,1024,1):
        MY_LED.duty(n)
        time.sleep(1)
        print(MY_LED)
        
    