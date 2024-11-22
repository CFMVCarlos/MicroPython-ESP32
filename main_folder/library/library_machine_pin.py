# Pins 1 and 3 are REPL UART TX and RX respectively
# Pins 6, 7, 8, 11, 16, and 17 are used for connecting the embedded flash, and are not recommended for other uses
# Pins 34-39 are input only, and also do not have internal pull-up resistors

# Pin.OUT: set the pin as an output
# Pin.IN: set the pin as an input

# Pin.PULL_UP: enable the internal pull-up resistor
# Pin.PULL_DOWN: enable the internal pull-down resistor
# Pin.OPEN_DRAIN: enable the open-drain output mode

# Pin.DRIVE_0: 5mA / 130 ohm
# Pin.DRIVE_1: 10mA / 60 ohm
# Pin.DRIVE_2: 20mA / 30 ohm (default strength if not configured)
# Pin.DRIVE_3: 40mA / 15 ohm

# Pin.IRQ_FALLING and Pin.IRQ_RISING: interrupt on falling or rising edge
# Pin.IRQ_LOW_LEVEL and Pin.IRQ_HIGH_LEVEL: interrupt on low or high level

from machine import Pin, Signal

# create an output pin on pin #0
p0 = Pin(0, Pin.OUT, Pin.PULL_DOWN, drive=Pin.DRIVE_3, value=0)

# set the value low then high
p0.value(0)
p0.value(1)

# create an input pin on pin #2, with a pull up resistor
p2 = Pin(13, Pin.IN, Pin.PULL_UP)

# read and print the pin value
print(p2.value())

# configure an irq callback
p2.irq(lambda p: print("Hello World!"), trigger=Pin.IRQ_FALLING)

#############################################
# Signal class

ps0 = Signal(Pin(0), invert=True)
ps0.off()

ps16 = Signal(Pin(16), invert=False)
ps16.on()
