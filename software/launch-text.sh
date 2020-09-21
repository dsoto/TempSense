#!/bin/bash

# create environment variable
export BLINKA_FT232H=1
# activate python custom library
source activate tempsense
# run text output program in python
python tempsense-text.py
