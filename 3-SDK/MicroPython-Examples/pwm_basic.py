from machine import Pin, PWM; P = Pin
from utime import sleep_ms

# Define the PWM LED as the Built IN LED Pin
led = PWM(P(25))
# Set the Frequency of the Clock
led.freq(10000)
# Infinite Loop
while True:
    # Function Pointer to the Sleep function
    s = sleep_ms
    # Create the Assending Range
    r = range(1,65535,100)
    # Loop Up
    for i in r:
        led.duty_u16(i)
        s(1)
    # Wait after Ascend
    s(100)
    # Create the Desending Range
    r = range(65535,1,-100)
    # Loop Down
    for i in r:
        led.duty_u16(i)
        s(1)
    # Wait after Decend
    s(600)
