# Future Work

The combination of CircuitPython libraries and a USB bridge open several possibilities for simple instruments.
Potential upgrades to this work include extending the software for direct cloud communications, installation on small single-board computers, more flexible USB bridge models, and other sensors.

Using Python extensions, data could be logged directly to an Excel or Google spreadsheet using available open-source libraries like gspread and xlwings and sent to cloud hosting services like Adafruit IO.
Derived quantities (temperature difference, heat transfer) could also be displayed in real time by extending the code and adding graph or text outputs.
The CircuitPython and USB bridge platform could also be extended to other platforms such as single-board computers (Raspberry Pi, BeagleBone) or embedded devices (Feather, Grand Central) providing a much more portable device.

Other USB bridge devices provide features that could enable the use of more SPI devices in a future upgrade.
The FTDI FT232H USB bridge supports only two (mode 0 and 2) of the four SPI modes.
Using another USB bridge supporting all four SPI modes would allow a wider range of sensors to be used.
A USB bridge device (e.g. MCP2210) that supports all 4 SPI modes would be compatible with the MAX 31865 amplifier allowing the use of high accuracy and precision RTD sensors.

A USB bridge device that supports all 4 SPI modes (for example the MCP2210) the SPI modes (1 and 3) used by the MAX 31865 chip would allow the use of high accuracy and precision RTD sensors.
As well, the MCP2210 uses the USB Human Interface Device (HID) protocol which could simplify the driver configuration and installation process.
The FTDI FT232H and other USB bridges also support the I2C protocol expanding the list of possible sensors.
CircuitPython maintains an extensive list of libraries to interface with SPI and I2C devices.
