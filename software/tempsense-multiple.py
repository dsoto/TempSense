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

# selects the metal pin to ask to talk with each board 
chip_select_1 = digitalio.DigitalInOut(board.D4)
chip_select_2 = digitalio.DigitalInOut(board.D5)
chip_select_3 = digitalio.DigitalInOut(board.D6)
chip_select_4 = digitalio.DigitalInOut(board.D7)

# creates an object speaking SPI, listening to a specific chip select, that measures temperature
temperature_sensor_1 = adafruit_max31855.MAX31855(spi, chip_select_1)
temperature_sensor_2 = adafruit_max31855.MAX31855(spi, chip_select_2)
temperature_sensor_3 = adafruit_max31855.MAX31855(spi, chip_select_3)
temperature_sensor_4 = adafruit_max31855.MAX31855(spi, chip_select_4)

# all the indented commands below run until the program is stopped
while True:

    # store temperature readings in memory for use by the computer
    temperature_1 = temperature_sensor_1.temperature
    temperature_2 = temperature_sensor_2.temperature
    temperature_3 = temperature_sensor_3.temperature
    temperature_4 = temperature_sensor_4.temperature

    # print the temperature readings to the screen
    print(datetime.datetime.now(), temperature_1, temperature_2, temperature_3, temperature_4)

    # wait for the desired measurement interval
    time.sleep(measurement_interval_seconds)


