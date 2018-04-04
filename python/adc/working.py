 #!/usr/bin/env python
#Caleb Hoke
# Analog Input with ADC0832 chip

import RPi.GPIO as GPIO
import ADC0832
import Adafruit_CharLCD as LCD
import subprocess
import time


lcd = LCD.Adafruit_CharLCDPlate()
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def IP(channel):
    global Select
    Select = False
def ADC(channel):
    global Select
    Select = True

GPIO.add_event_detect(24, GPIO.FALLING, callback=IP, bouncetime=300)
GPIO.add_event_detect(23, GPIO.FALLING, callback=ADC, bouncetime=300)

while True:
 IP = subprocess.check_output(['hostname','-I'])
 if len(IP) > 8:
  break
 else:
  time.sleep(2)


Name = subprocess.check_output(['hostname']).strip()
displayText = IP + Name
Select = False
oldmessage = None


try:
    while True:
        if Select:
            value = ADC0832.getADC(0)
            VoltText = 'current voltage\n %f' % value
            Thismessage = VoltText
        else :
            Thismessage = displayText
        if oldmessage == Thismessage:
            pass
        else:
            lcd.clear()
            lcd.message(Thismessage)
            oldmessage = Thismessage
        time.sleep(0.2)



except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()