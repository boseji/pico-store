from machine import Pin, UART;P=Pin
from utime import sleep_ms

# Create the Correct UART with Baudrate of 115200
# Tested UART0: GP0=TX GP1=RX
#uart = UART(0, 115200)
# Tested UART1: GP4=TX GP5=RX
#uart = UART(1, 115200,tx=P(4),rx=P(5))
# Tested UART1: GP8=TX GP9=RX
uart = UART(1, 115200,tx=P(8),rx=P(9))
# connect the USB-Serial board sould connect to that accordingly.

# Buffer for reading 1 Byte of Data
buf = bytearray(1)
# Function Pointer to the uart.any for quick use
rx = uart.any
# Empty Rx Buffer to Load the received data
n = bytearray(0)

# Mark The Beginning
print("Starting UART Echo")
uart.write("\nStarting UART Echo\n")
# Infinite Loop
while True:
    # Wait till some data is available on the UART
    if rx() == 1 :
        # Read 1 Byte of Data
        uart.readinto(buf)
        # Append it the Rx buffer
        n.append(buf[0])
        # Wait till we read a '\n' New line
        if buf[0] == 10:
            #print(n)
            uart.write(n)
            # Clean up the Rx Buffer to receive new data
            n = bytearray(0)
#    print('.', end='')
#    sleep_ms(100)           # Sleep for 100mS

