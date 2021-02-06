from machine import Pin,UART; P = Pin

# Configure the Onboard LED
led = P(25, P.OUT)
# Configure the Button for Active High Input
button = P(22, P.IN, P.PULL_DOWN)
# Get the UART1 of specific pins
uart = UART(1, 115200,tx=P(8),rx=P(9))

# Button Handler ISR function
def button_handler(pin):
    # Check if we have received the correct button or not
    if pin == button:
        # De-register handler after First Press
        pin.irq(handler=None)
        # Light Up the LED
        led.value(1)
        uart.write('Pressed\n')
    
# Main
# Turn Off the LED
led.value(0)
# Setup the ISR
button.irq(trigger=P.IRQ_RISING, handler=button_handler)
