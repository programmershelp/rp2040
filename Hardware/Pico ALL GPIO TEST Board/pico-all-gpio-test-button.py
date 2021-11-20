from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(12, Pin.IN, Pin.PULL_UP)
button1 = Pin(13, Pin.IN, Pin.PULL_UP)
button2 = Pin(14, Pin.IN, Pin.PULL_UP)
button3 = Pin(16, Pin.IN, Pin.PULL_UP)
button4 = Pin(17, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() & button1.value() & button2.value() & button3.value() & button4.value() :                       
	    led.low()
	    time.sleep(0.5)
    elif button.value() | button1.value() | button2.value() | button3.value() | button4.value() :
        led.high()
        time.sleep(0.5)



