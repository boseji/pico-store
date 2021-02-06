import machine
import utime

# Button is Input on GP14
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
# Use the Onboard LED to show status
led_onboard = machine.Pin(25, machine.Pin.OUT)

# Infinite Loop
while True:
    if button.value() == 1:  # Check if the Button was pressed
        led_onboard.value(1) # Set LED ON if the Button was pressed
        utime.sleep(0.1)     # Wait for 100mS
    else:
        led_onboard.value(0) # If not pressed Turn Off LED
