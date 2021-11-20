from machine import Pin
import time

led=[28,27,1,0,22,21,3,2,20,19,5,4,15,18,7,6,11,10,9,8];

Pin(led[0], Pin.OUT)
Pin(led[1], Pin.OUT)
Pin(led[2], Pin.OUT)
Pin(led[3], Pin.OUT)
Pin(led[4], Pin.OUT)
Pin(led[5], Pin.OUT)
Pin(led[6], Pin.OUT)
Pin(led[7], Pin.OUT)
Pin(led[8], Pin.OUT)
Pin(led[9], Pin.OUT)
Pin(led[10], Pin.OUT)
Pin(led[11], Pin.OUT)
Pin(led[12], Pin.OUT)
Pin(led[13], Pin.OUT)
Pin(led[14], Pin.OUT)
Pin(led[15], Pin.OUT)
Pin(led[16], Pin.OUT)
Pin(led[17], Pin.OUT)
Pin(led[18], Pin.OUT)
Pin(led[19], Pin.OUT)


while 1:
    for i in range(len(led)):
        j=Pin(led[i], Pin.OUT)
        Pin(led[0], Pin.OUT).low()
        Pin(led[1], Pin.OUT).low()
        Pin(led[2], Pin.OUT).low()
        Pin(led[3], Pin.OUT).low()
        Pin(led[4], Pin.OUT).low()
        Pin(led[5], Pin.OUT).low()
        Pin(led[6], Pin.OUT).low()
        Pin(led[7], Pin.OUT).low()
        Pin(led[8], Pin.OUT).low()
        Pin(led[9], Pin.OUT).low()
        Pin(led[10], Pin.OUT).low()
        Pin(led[11], Pin.OUT).low()
        Pin(led[12], Pin.OUT).low()
        Pin(led[13], Pin.OUT).low()
        Pin(led[14], Pin.OUT).low()
        Pin(led[15], Pin.OUT).low()
        Pin(led[16], Pin.OUT).low()
        Pin(led[17], Pin.OUT).low()
        Pin(led[18], Pin.OUT).low()
        Pin(led[19], Pin.OUT).low()
        
        
        time.sleep(0.1)
        j.high()
        time.sleep(0.1)

    





        





