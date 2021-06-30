#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
read_mavlink.py: Read mavlink messeges directly from the FCU

"""

from pymavlink import mavutil
import time

interface = mavutil.mavlink_connection("/dev/ttyACM0", baud=57400, autoreconnect=True)
#interface = mavutil.mavlink_connection("udp:127.0.0.1:14550", autoreconnect=True)
#interface = mavutil.mavlink_connection("/tmp/PX2", baud=57600, autoreconnect=True)

while True:
    m = interface.recv_msg()
    #print(m)
    if m:
        #print(m)
        if (m.get_type() == 'GLOBAL_POSITION_INT'):
            print(m)
