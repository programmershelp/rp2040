import time
import board
import adafruit_vcnl4040
import busio

# Create sensor object, communicating over the board's default I2C bus
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
sensor = adafruit_vcnl4040.VCNL4040(i2c)

while True:
    print("Proximity:", sensor.proximity)
    print("Light: %d lux" % sensor.lux)
    time.sleep(1.0)