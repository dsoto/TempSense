import time                   # this library allows program to pause
import board                  # this library defines the metal pins on the board
import busio                  # this library allows us to speak SPI
import digitalio              # this library lets us turn metal pins on and off 
import adafruit_max31855      # this library know how to talk to the temperature board
import datetime               # this library knows the clock and the calendar

# the number of seconds between measurements
measurement_interval_seconds = 1

# creates channel to "speak" SPI
# tells which metal pins on the bridge board help us speak SPI
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# sets pin on board to signal to amplifier to speak SPI
# on the 4-channel board, you can use D4, D5, D6, or D7
cs = digitalio.DigitalInOut(board.D4)

# python object that knows how to get temperatures from amplifier
temperature_sensor = adafruit_max31855.MAX31855(spi, cs)

while True:

    # print date, time, and temperature to screen
    print(datetime.datetime.now())

    # by writing ".temperature" we ask the board for a reading
    print(temperature_sensor.temperature)

    # wait for one second
    time.sleep(measurement_interval_seconds)

