#!/bin/bash

export BLINKA_FT232H=1
source activate ph2020
bokeh serve --show ft232h-logger-spi.py
