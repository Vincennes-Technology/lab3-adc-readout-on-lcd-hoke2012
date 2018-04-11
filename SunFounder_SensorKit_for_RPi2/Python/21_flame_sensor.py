#!/usr/bin/env python
#Caleb Hoke
#------------------------------------------------------------------------------
#https://www.sunfounder.com/learn/lesson-21-flame-sensor-sensor-kit-v2-0-for-b-plus.html
#Flame sensor A0 to PCF8591 AIN0
#Flame sesnro D0 to GPIO 17
#PCF8591 SCL to GPIO 5
#PCF8591 SDA to GPIO 3
#


import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math
import Adafruit_CharLCD as LCD
import subprocess
import socket

SERVERIP = '10.0.0.43'
condition = "Safe"
lcd = LCD.Adafruit_CharLCDPlate()

DO = 17
GPIO.setmode(GPIO.BCM)
def setup():
    ADC.setup(0x48)
    GPIO.setup(DO, GPIO.IN)

def Print(x):
    if x == 1:
        condition = "Safe"
        y = "safe"
        print ''
        print '   *********'
        print '   * Safe~ *'
        print '   *********'
        print ''
        lcd.clear()
        lcd.message("Safe~\n")

    else:
        condition = "Fire"
        print ''
        print '   *********'
        print '   * Fire! *'
        print '   *********'
        print ''
        lcd.clear()
        lcd.message("Fire!\n")
    return condition

def loop():
    status = 1
    n = 0
    tmp = GPIO.input(DO);
    condition = Print(tmp)
    while True:
        print ADC.read(0)
        tmp = GPIO.input(DO);
        if tmp != status:
            condition = Print(tmp)
            status = tmp
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((SERVERIP, 8881))
        print "%d : Connected to server" % n,
        data = "%s,'Flame Sensor','%d', %s" % (n, ADC.read(0), condition)
        sock.sendall(data)
        print " Sent:", data
        sock.close( )
        n += 1
        time.sleep(6)
if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        pass