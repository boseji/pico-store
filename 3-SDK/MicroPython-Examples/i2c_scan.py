# Program to Scan for I2C devices

# Import only what is needed and alias them if possible
from machine import Pin,I2C; P = Pin

# Scan function
def scan(i,sda,scl):
    # P(scl) - actually creats the machine.Pin(scl) Its just shortened.
    # Also scan() function is directly used to reduce allocation.
    ar = I2C(i,scl=P(scl),sda=P(sda),freq=100000).scan()
    # Array interpolation to print in the Pretty form in multiple
    # formats.
    return [ '{0} = 0x{0:02x} = 0b{0:b}'.format(i) for i in ar ]

## Main Program

print('I2C scanned devices: ')
# Just print the Scanned Values
# - We using GP12 as SDA and GP13 as SCL
print(scan(0,12,13))