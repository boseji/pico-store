# For GPIO LED
from machine import Pin as P
# For Thread creation method
from _thread import start_new_thread as T
# For Sleep
from utime import sleep_ms as S

# Core 1 Task to be executed
def core1_task():
    # Get function Pointer to Value function for OnBoard LED
    l = P(25, P.OUT).value
    # Infinite Loop - Core 1
    while True:
        l(1)
        S(200)
        l(0)
        S(200)

# Main
i = 0
print("Starting Multi Core Demo !")
# Fork the Task to Core1 - No Arguments
T(core1_task, ())
# Infinite Loop - Core0
while True:
    print("This is From the Main Loop on Core0 -", i)
    S(100)
    i += 1
