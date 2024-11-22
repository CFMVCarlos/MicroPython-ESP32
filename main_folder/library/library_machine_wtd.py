import time

from machine import WDT

# Create a WDT object with a timeout of 2 seconds
wdt = WDT(timeout=2000)

try:
    while True:
        # Perform some tasks here...

        # Feed the watchdog periodically to prevent it from expiring
        wdt.feed()

        # Simulate some processing time
        time.sleep_ms(500)

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    name = input("Enter your name: ")
    print("Hello, " + name + "!")
