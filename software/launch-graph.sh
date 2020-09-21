#!/bin/bash

# create environment variable
export BLINKA_FT232H=1
# activate python custom library
source activate tempsense
# run graphing program using bokeh server
bokeh serve --show tempsense-graph.py
