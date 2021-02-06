from micropython import const
# For GPIO LED
from machine import Pin, UART; P = const(Pin)
# For Thread creation method
from _thread import start_new_thread as T
# For Sleep
from utime import sleep_ms as S

# Register Global Var
global RxC
RxC:bool = False
# Empty Rx Buffer to Load the received data
global RxB
RxB = bytearray(0)

# Core 1 Task to be executed
def core1_task():
    # Initialize the UART
    u = UART(1, 115200,tx=P(8),rx=P(9)) 
    # Get function Pointer to Value function for OnBoard LED
    l = P(25, P.OUT).value
    # Buffer for reading 1 Byte of Data
    buf = bytearray(1)
    # Function Pointer to the uart.any for quick use
    rx = u.any
    # Get Handle on Global Vars
    global RxC
    global RxB
    # Start-up message
    u.write('\nStarting Multi Core UART Echo demo!\n')
    # Infinite Loop - Core 1
    while True:
        if not RxC:
            # Wait till some data is available on the UART
            if rx() == 1 :
                # Read 1 Byte of Data
                u.readinto(buf)
                # Append it the Rx buffer
                RxB.append(buf[0])
                # Wait till we read a '\n' New line
                if buf[0] == 10:
                    # Signal We are Done
                    RxC = True

# Main
print('\nStarting Multi Core UART Echo demo!')
# Fork the Task to Core1 - No Arguments
T(core1_task, ())
# Infinite Loop - Core0
while True:
    # If we received any Data
    if RxC:
        # Print the Rx Buffer
        print("\nGot Data: ",RxB.decode('ascii'))
        # Clear It
        RxB = bytearray(0)
        # Signal Complete
        RxC = False
    else:
        # Blank to Keep Alive
        print(" ", end='')
    S(1000)
    