from machine import ADC; A = ADC
from utime import sleep
# Conversion Factor
C = 3.3 / 65535
# Get the Temperature Sensor on Channel 4
# We directly get the function Pointer to the read_u16 function
t = ADC(4).read_u16

while True:
    # Voltage Reading
    r = t() * C
    print('Voltage: ',r)
    # Convert the Voltage to Temperature
    tr = 27 - (r - 0.706)/0.001721
    print('Temperature: ',tr,'decC')
    sleep(2)