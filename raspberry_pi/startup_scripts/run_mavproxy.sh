#!/bin/bash

screen -d -m -S "mavproxy.$(hostname)" \
    mavproxy.py --aircraft=copter \
    --master=/dev/ttyACM0 --baudrate=115200 \
    --state-basedir=/home/pi/custom_aircraft/logs \
