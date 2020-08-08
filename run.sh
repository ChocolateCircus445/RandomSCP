#!/bin/bash
# The number after the -p is the port this will be running on.
# I don't think 5168 will conflict with anything, but you can
# change the port number if you want to.
export FLASK_APP=randomscp.py
python3 -m flask -p 5168
