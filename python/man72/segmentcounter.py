#!/usr/bin/python
#Caleb Hoke
#man72 connected to mcp23017 counter
# 25 April 2018

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                    \\\\INSTRUCTIONS////
#////////////////////////////////////////////////////////////////
#******Before beginning, open terminal and run "sudo pip install smbus2"******
#* Run "sudo i2cdetect -y 1" to ensure that the device is detected by your I2C
#******This project identifies the installed device under address "0x22"
#  yours may be different, if so then change anywhere addressed to "0x22"
#  to the address presented when you run "sudo pip install smbus2"


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#             \\\\    MCP23017 pinout    ////
#//////////////////////////////////////////////////////////////////
#pinout for mcp23017 to adc using the port "B":
# pin 1 of mcp to 6 of man72
# pin 2 of mcp to 11 of man72
# pin 3 of mcp to 2 of man72
# pin 4 of mcp to 7 of man72
# pin 5 of mcp to 8 of man72
# pin 6 of mcp to 10 of man72
# pin 7 of mcp to 13 of man72
# pin 8 of mcp to 1 of man72
# pin 9 of mcp to 5volt connection
# pin 10 of mcp to ground
# pin 12 of mcp to TCobbler SCL (5)
# pin 13 of mcp to TCobbler SDA (3)
# pin 15 of mcp to ground
# pin 16 of mcp to 10k resistor to 5 volts
# pin 17 of mcp to ground
# pin 18 of mcp to 10k resistor to 5 volts
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#               \\\\    Man72 pinout    ////
#//////////////////////////////////////////////////////////////////
# pin 3 of man72 to 5 volts
# pin 9 of man72 to 5 volts
# pin 14 of man72 to 5 volts
# 1=dp, 6=g, 5=f, 4=e, 3=d, 2=b, 1=c, 0=a
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#
#//////////////////////////////////////////////////////////////////

import smbus2
import time

bus = smbus2.SMBus(1)
# For revision 1 Raspberry Pi, change to bus = smbus.SMBus(1) for revision 2.

#          0      1     2    3     4     5     6     7    8     9
decode = [0x02, 0x9E, 0x24, 0x0C, 0x98, 0x48, 0xC0, 0x1E, 0x00, 0x18]


address = 0x22  # I2C address of MCP23017
bus.write_byte_data(0x22, 0x00, 0x02)  # Set all of bank A to outputs
bus.write_byte_data(0x22, 0x01, 0x02)  # Set all of bank B to outputs
time.sleep(1)

while True:
    for digit in range(0, 10):
        bus.write_byte_data(0x22, 0x01, 0x02)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x01, 0x9E)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x01, 0x24)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x01, 0x0C)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x01, 0x98)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x01, 0x48)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x01, 0xC0)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x01, 0x1E)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x01, 0x00)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x01, 0x18)
        time.sleep(1)





