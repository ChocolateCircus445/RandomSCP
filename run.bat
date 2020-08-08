rem The number after the -p is the port this will be running on.
rem I don't think 5168 will conflict with anything, but you can
rem change the port number if you want to.
set FLASK_APP=randomscp.py
python -m flask -p 5168
