from machine import Pin
import uasyncio

# Define the Global Pin
led=Pin(25, Pin.OUT)

# Coroutine that would execute in async
async def blink(led, period_ms):
    while True:
        led.high()
        await uasyncio.sleep_ms(5)
        led.low()
        await uasyncio.sleep_ms(period_ms)

# Async Main Task that has limited running time
async def main():
    global led
    uasyncio.create_task(blink(led,900))
    for i in range(1,11):
        await uasyncio.sleep_ms(1000)
        print("Still running! -", i)

# Run the Main async-task
uasyncio.run(main())
print("Done with all Tasks!")