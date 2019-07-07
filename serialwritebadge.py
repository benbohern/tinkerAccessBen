#!/usr/bin/env python
          
import time
import serial
          
      
ser = serial.Serial(
              
               port='/dev/ttyUSB0',
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )
counter=0
          
print "12345"      
ser.write('12345\n')




session_seconds = 60
login_response = {
            'user_name': "Ben",
            'device_name': "shopbot",
            'user_id': "12345",
            'badge_code': "12345",
            'session_seconds': session_seconds,
            'remaining_seconds': session_seconds,
            'remaining_extensions': 2,
        }

if login_response.get('remaining_seconds') > 0:
            print ">0"
else:
            print "0"
