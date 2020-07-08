# Temperature Logger

This is a simple multi-channel temperature logger board and real-time display application.

The temperature logger uses temperature sensors with a digital interface that responds to requests for data over serial and is implemented in CircuitPython.

The real-time display uses a python streaming graphing app (Bokeh) to request temperature data from the logger board and post to a graph on a laptop or computer.

# Mapping Sensors

The sensors in the legend are specified by the pin used for the chip select.
This pin is visible on the silkscreen of the feather board.

# Running

The command below exports the environment variable, activates the python environment with libraries, and runs the script.

> ./launch-logger

# Circuit Python Installation

> pip install adafruit-blinka
> pip install adafruit-circuitpython-busdevice
> pip install adafruit-circuitpython-max31865

I haven't resolved if I need the local copy of adafruit_max31855.py

# FTDI stuff

It is unclear if you need the FTDI driver installed or if a clean install can support the FT232H.

Notes from recent attempt:

I found and removed an FTDIUSBSerialDriver.kext file in /Library/Extensions while leaving the FTDI driver in /System/Library/Extensions and it is working.