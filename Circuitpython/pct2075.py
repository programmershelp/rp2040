import time
import board
import adafruit_pct2075
import busio

# Create sensor object, communicating over the board's default I2C bus
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
pct = adafruit_pct2075.PCT2075(i2c)

while True:
    print("Temperature: %.2f C" % pct.temperature)
    time.sleep(0.5)