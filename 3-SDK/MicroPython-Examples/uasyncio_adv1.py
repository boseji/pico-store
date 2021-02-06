from micropython import const
from machine import Pin, UART
from uasyncio import new_event_loop, sleep_ms, Event

# Get the Handle on Execution Loop
mloop = new_event_loop()
# Create Receive Event
# - https://docs.micropython.org/en/latest/library/uasyncio.html#class-event
rxevt = Event()

# Serial Port Coroutine
async def serialcoro():
    # Create the Serial Port
    s = UART(1, 115200,tx=Pin(8),rx=Pin(9))
    # Function Pointer to the s.any for quick use
    ready = s.any
    # Serial Coroutine Loop - Wait until something is
    #  received on UART
    while ready() != 1:
        # Async Sleep for some time
        await sleep_ms(100)
        # Keep the REPL Active
        print(' ',end='')
    # We are Out of the Loop hence we have something in the Receive Buffer
    global rxevt
    rxevt.set() # Signal the Receive Event
    print("\nReceived data on UART !")

# Main Coroutine
async def main():
    global mloop, rxevt
    # Create the Task
    mloop.create_task(serialcoro())
    # Wait on the Receive Event to be Raised
    await rxevt.wait()
    # Stop the Main Loop
    mloop.stop()
    # we Are done
    print("\nStopping Execution")

# Begin Execution
print("Starting Loop")
mloop.run_until_complete(main())
