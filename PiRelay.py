#!/usr/bin/python

# Library for PiRelay
# Developed by: SB Components
# Author: Ankur,JKarthaus
# Project: PiRelay
# Python: 3.4.2
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

class Relay:
    ''' Class to handle Relay

    Arguments:
    relay = string Relay label (i.e. "RELAY1","RELAY2","RELAY3","RELAY4")
    '''
    relayGpio = {"RELAY1":19, "RELAY2":13, "RELAY3":6, "RELAY4":5}


    def __init__(self, relay):
        self.pin = self.relayGpio[relay]
        self.relay = relay
        GPIO.setup(self.pin,GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def on(self):
        print(self.relay + " - ON")
        GPIO.output(self.pin,GPIO.HIGH)

    def off(self):
        print(self.relay + " - OFF")
        GPIO.output(self.pin,GPIO.LOW)
