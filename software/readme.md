# TempSense Temperature Logger

This is a simple multi-channel temperature logger board and real-time display application.

The temperature logger uses temperature sensors with a digital interface that responds to requests for data over serial and is implemented in CircuitPython.

The real-time display uses a python streaming graphing app (Bokeh) to request temperature data from the logger board and post to a graph on a laptop or computer.

# Running

The included shell scripts export the environment variable, activate the python environment with libraries, and run the script.

# Installation

The libraries for running these scripts can be installed with the conda package manager and environment file.

> conda env create -f tempsense-environment.yml
