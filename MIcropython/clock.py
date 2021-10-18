import math
import utime
import picoscroll as scroll
from machine import Pin

scroll.init()

secupdated = False
led = Pin(25,Pin.OUT)

# Initial time, from RTC if set via the shell, or 12:30:01 otherwise (if RTC is unset, epoch is 1/1/21 00:00:01)
if utime.localtime()[0] == 2021 and utime.localtime()[1] == 1 and utime.localtime()[2] == 1:
    hours = 12
    minutes = 30
    seconds = 1
    sync = False
    led.low()
else:
    hours = utime.localtime()[3]
    minutes = utime.localtime()[4]
    seconds = utime.localtime()[5]
    sync = True
    led.high()

# LED Brightness (0-255)
brightness = 50

# Character pixel maps (3w x 5h font)
zero = [0,1,1,1,0],[1,0,0,0,1],[0,1,1,1,0]
one = [0,1,0,0,1],[1,1,1,1,1],[0,0,0,0,1]
two = [1,0,0,1,1],[1,0,1,0,1],[0,1,0,0,1]
three = [1,0,1,0,1],[1,0,1,0,1],[0,1,0,1,0]
four = [0,1,1,1,0],[1,0,0,1,0],[0,0,1,1,1]
five = [1,1,1,0,1],[1,0,1,0,1],[1,0,0,1,0]
six = [0,1,1,1,0],[1,0,1,0,1],[0,0,0,1,0]
seven = [1,0,0,1,1],[1,0,1,0,0],[1,1,0,0,0]
eight = [0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0]
nine = [0,1,0,0,0],[1,0,1,0,1],[0,1,1,1,0]
error = [1,1,1,1,1],[1,0,1,0,1],[1,0,1,0,1]
charlist = [zero,one,two,three,four,five,six,seven,eight,nine]

# Draw characters using above pixel maps, left to right, top to bottom
def draw_digit(x,y,map):
    global brightness

    scroll.set_pixel(x,y,map[0][0]*brightness)
    scroll.set_pixel(x+1,y,map[1][0]*brightness)
    scroll.set_pixel(x+2,y,map[2][0]*brightness)

    scroll.set_pixel(x,y+1,map[0][1]*brightness)
    scroll.set_pixel(x+1,y+1,map[1][1]*brightness)
    scroll.set_pixel(x+2,y+1,map[2][1]*brightness)

    scroll.set_pixel(x,y+2,map[0][2]*brightness)
    scroll.set_pixel(x+1,y+2,map[1][2]*brightness)
    scroll.set_pixel(x+2,y+2,map[2][2]*brightness)

    scroll.set_pixel(x,y+3,map[0][3]*brightness)
    scroll.set_pixel(x+1,y+3,map[1][3]*brightness)
    scroll.set_pixel(x+2,y+3,map[2][3]*brightness)

    scroll.set_pixel(x,y+4,map[0][4]*brightness)
    scroll.set_pixel(x+1,y+4,map[1][4]*brightness)
    scroll.set_pixel(x+2,y+4,map[2][4]*brightness)
    return

# Process clock characters
def character(x,y,char):
    global charlist
    if char &gt;= 0 and char &lt;=9:
        draw_digit(x,y,charlist[char])
        return
    else:
        draw_digit(x,y,error)
        return

# Act on button presses
def buttonhandler():
    global hours, minutes, brightness, led
    
    if scroll.is_pressed(scroll.BUTTON_A):
        led.low()
        if scroll.is_pressed(scroll.BUTTON_X):
            if brightness &lt;= 245 and brightness &gt;= 10:
                brightness += 10
            elif brightness &lt; 255 or brightness &lt; 10:
                brightness += 1
        else:
            hours += 1
        return

    if scroll.is_pressed(scroll.BUTTON_B):
        led.low()
        if scroll.is_pressed(scroll.BUTTON_Y):
            if brightness &gt;= 11 and brightness &lt;= 250:
                brightness -= 10
            elif brightness &gt; 3 or brightness &gt; 250 :
                brightness -= 1
        else:
            hours -= 1
            if hours &lt; 0:
                hours = 23
        return


    if scroll.is_pressed(scroll.BUTTON_X):
        led.low()
        minutes += 1
        return

    if scroll.is_pressed(scroll.BUTTON_Y):
        led.low()
        minutes -= 1
        if minutes &lt; 0:
            minutes = 59
        return

def draw_clock(hrs,mins,secs):
    global brightness
    scroll.clear()

    character(0,0,hrs//10) # hour tens (0-2)
    character(4,0,hrs%10) # hour units (0-9)
    character(10,0,mins//10) # minute tens (0-5)
    character(14,0,mins%10) # minute units (0-9)

    if(secs % 2 != 0): # draw colon between hours and minutes on odd seconds
        scroll.set_pixel(8,1,brightness)
        scroll.set_pixel(8,3,brightness)
        
    # seconds pixel bar across the bottom - borrowed from the scrollphathd clock example
    seconds_progress = 15 * ((secs % 60) / 59.0)
    for y in range(15):
        current_pixel = min(seconds_progress, 1)
        scroll.set_pixel(y + 1, 6, int(current_pixel * brightness))
        seconds_progress -= 1
        if seconds_progress &lt;= 0:
            break
            
    scroll.update()

# Main clock loop
while True:
    utime.sleep(0.5)
    seconds = utime.localtime()[5]

    buttonhandler()
    
    if seconds == 0 and secupdated == False:
        minutes += 1
        secupdated = True
        
    if seconds == 1 and secupdated == True:
        secupdated = False

    if minutes &gt; 59:
        hours += 1
        minutes = 0

    if hours &gt; 23:
        hours = 0

    draw_clock(hours,minutes,seconds)