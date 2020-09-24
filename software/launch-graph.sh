#!/bin/bash

# create environment variable
# set BLINKA_FT232H=1    # command for windows
export BLINKA_FT232H=1   # command for linux and os x

# activate python custom library
conda activate tempsense

# run graphing program using bokeh server
bokeh serve --show tempsense-graph.py
