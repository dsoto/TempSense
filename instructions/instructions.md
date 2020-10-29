# Build instructions

## Hardware

When you place your order for the bill of materials, decide if you want unshielded or shielded thermocouples or both. Shielded thermocouples are best for measurements of liquids.
You can order the PCB through OSHPark by uploading the `TempSense.kicad_pcb` file and specifying a 2-layer PCB board.
Alternately, the circuit can be built on a solderless breadboard since the number of connections is tractable.
Once you have received the PCB, you can begin the required soldering of the pins and pin receptacles to the custom PCB and the amplifier circuit boards.
Before assembly, take the usual safety measures for soldering including caution around hot objects, adequate ventilation from flux fumes, eye protection from flux or solder spatter, and low-toxicity lead-free solder.

Start by assembling the USB bridge board and the thermocouple amplifiers.
Solder the two 10-pin header strips included with the part to the FT232H USB bridge board.
For all pins and receptacles, start by soldering one pin and then verify that the pin strip is perpendicular to the PCB before continuing.
Solder the 6-pin header strip to each of your thermocouple amplifier boards.
Solder the terminal blocks to each of the thermocouple amplifier boards.
Verify the wires will enter from the outside of the board before soldering.

Next, solder the receptacles on to the custom PCB and insert the components.
Solder the two 10-pin socket strips to the circuit board to create the USB bridge connection in the U5 area.
Solder a 6-pin socket strip to the printed circuit board in the U1--U4 areas.
Insert the USB bridge in the U5 position and be sure the USB port is facing the small rectangle near the U5 text.

The orientations of the circuit boards are shown in the photo.
Insert the thermocouple amplifiers into the U1--U4 sockets.
With the thermocouple amplifiers inserted, you can attach the thermocouples.
Note the designations for thermocouple polarities on the thermocouple amplifier board.
Note that not all thermocouples follow the color convention and that a reversed thermocouple will give a lower reading with higher temperatures.

![Assembled instrument and bare printed circuit
board.](../figures/tempsense-v0p2-photo.jpg){#fig:photo width="90%"}

## Software environment

The instrument requires the installation of several software libraries that translate the Python commands in the scripts to the digital signals to read temperatures from the thermocouple amplifiers.
We first install the TempSense library containing the scripts for reading and recording temperatures.
The linked Mendeley Data repository contains these scripts. Place the software folder in a convenient location on your hard drive.

Next we install the libraries to translate the Python scripts to commands for the USB bridge and thermocouple amplifiers.
We start with a Python/CPython installation for your host computer.
Many computers include Python/CPython, but it is useful to install a Python implementation that allows the creation of custom environments with installed libraries that can be activated or deactivated.
An excellent option for installing Python with these environments is the Anaconda Individual Python distribution or the Miniconda distribution.
Anaconda is a multi-gigabyte distribution containing many libraries for scientific computation while the Miniconda distribution is a minimal distribution that can be expanded.
These distributions provide the Python language and also an installer (conda) that we use to install other Python software in custom environments.
Navigate to the websites for these installations and follow the instructions for your host computer operating system.
With the Python software installed, you can proceed to the creation of the custom software environment for the tool.

The Mendeley Data repository contains the file, `tempsense-environment.yml`.
When run, this file downloads and installs the necessary libraries between the Python scripts and USB bridge and places them in an environment named tempsense.
Navigate to the directory containing the file in the command line and execute the following command.

    > conda env create -f tempsense-environment.yml

At this point the libraries are installed and we move on to the verification of their installation and the links between them.

We start by verifying the presence of our custom python environment, tempsense.
Activate the tempsense environment and view the installed libraries by typing the following commands.
Note that some systems may use `source activate tempsense` or `activate tempsense` instead.

    > conda activate tempsense
    > conda list

If you see a listing of several packages, Python/CPython and the custom environment have been installed correctly.

To verify that the Python and C USB libraries (pyusb and libusb) are correctly configured and can connect to the USB bridge, activate the tempsense environment and open a Python interpreter by typing python at the command line, then plug in the TempSense device to the host computer and type the following.

    >>> import usb
    >>> import usb.util
    >>> dev = usb.core.find(idVendor=0x0403, idProduct=0x6014)
    >>> print(dev)

If you see a text table describing the device without errors, this is configured correctly.

To verify that the Python library to communicate with the FTDI bridge over USB is correctly configured type the following in a Python interpreter with the tempsense environment activated.

    >>> import pyftdi.ftdi
    >>> pyftdi.ftdi.Ftdi.list_devices()

You should see a listing for the connected FTDI USB bridge device verifying that the pyftdi library is installed.

If you have problems, the most common issues involve the C USB drivers.
On Windows, Zadig is a free tool for associating a driver with the USB bridge.
You may need to manually install the C USB library, libusb by visiting the website and downloading.
More extensive troubleshooting and detailed instructions for OS X, Linux, and Windows can be found in the FT232H tutorial on the Adafruit site.

In the last step of the installation and configuration we create an environment variable to instruct the CircuitPython library of the type of hardware (the USB bridge) it will be sending instructions to.
If you are comfortable setting environment variables, you can include it in a start-up script for your computer.
Otherwise, we set the environment variable before each use of the instrument by typing the following in the comand line.
Note some machines use a different command than export (Some Windows shells use set).

    > export FT232H_Blinka=1

To ensure that the CircuitPython library, Blinka compatibility layer, and environment variable are correctly configured type the following in a python interpreter with the tempsense environment activated and the device plugged in.

    >>> import board

If this runs without an error, the CircuitPython libraries are connected and you are ready to run the instrument.

# Operation instructions

To operate the instrument, we configure the Python scripts with our time intervals or other customizations, decide on text or graph output, and run the shell script to set the environment variable and run the appropriate Python script.
Open the script in a text editor and set the measurement interval in the Python scripts to set the time interval between samples and comment out any code to read or display any sensors you aren't using.
You can also set the variable for the location of any log files you generate.

Place the sensors in the desired locations while using caution when placing probes on hot surfaces or in hot areas.
Next we choose the text output program or the graphing program and launch the appropriate shell script.
These launch scripts activate the tempsense environment, set the environment variable for the USB bridge, and run the Python commands script.
In both cases, the same commands activate the custom python environment and set the environment variable as in the installation and testing.
For the text script, we run with a python command `python tempsense-text.py`.
For the graph script, we run with a bokeh command `bokeh serve --show tempsense-graph.py`.
These three commands are placed in script files for convenience.
The files are written for UNIX-like systems and may need to be revised for other operating systems.

Run the launch script for text output by typing

    > sh launch-text.sh

You should see a text listing of time stamps and temperature
observations output to the console.

To run the real-time graphing application, run the launch script by typing

    > sh launch-graph.sh

You should see a browser window open with a graph window.
To end the programs, type Ctrl-C in the console window to interrupt the program.

![Graphing in Browser Window](../figures/graph-screenshot.png)