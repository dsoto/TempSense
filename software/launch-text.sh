#!/bin/bash

# create environment variable
# set BLINKA_FT232H=1    # alternate command for windows
export BLINKA_FT232H=1   # command for linux and os x

# activate python custom library
# source activate tempsense  # alternate command
conda activate tempsense

# run text output program in python
python tempsense-text.py
