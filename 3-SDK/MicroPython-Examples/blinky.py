import machine
import utime

# On-board LED is on GP25
led_onboard = machine.Pin(25, machine.Pin.OUT)

# Infinite Loop
while True:
    led_onboard.value(1) # Set the LED to ON
    utime.sleep(0.2)     # Delay 200 mS
    led_onboard.value(0) # Set the LED to OFF
    utime.sleep(0.2)     # Delay 200 mS