from machine import Pin, UART;P=Pin
from utime import sleep_ms

# Create the Correct UART with Baudrate of 115200 and
# selecting UART0 peripheral of the RP2040
# We are using GP12 as TX and GP13 as RX hence the USB-Serial
# board sould connect to that accordingly.
uart = UART(0, 115200, tx=P(12), rx=P(13))

# Infinite Loop
while True:
    uart.write('Hari Aum\n') # Send the Welcome
    sleep_ms(1000)           # Sleep for 1 second

