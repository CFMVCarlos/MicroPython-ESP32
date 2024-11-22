# Import necessary modules
import time
import micropython
from machine import Pin

# Allocate buffer for emergency exception handling (useful for debugging)
micropython.alloc_emergency_exception_buf(100)

# Initialize variables
button_presses = 0  # the count of times the button has been pressed
last_time = 0  # the last time the button was pressed


def button_pressed_handler(pin):
    """
    This handler is called when the button is pressed. It increments the
    button_presses count and implements a basic debounce mechanism.
    """
    global button_presses
    # Disable the IRQ during debounce check to avoid re-triggering the handler
    pin.irq(handler=None)
    button_presses += 1  # Increment the button press count
    # Implement debounce - we ignore any button activity during this period
    time.sleep_ms(200)  # Sleep for 200 ms to allow the debounce time
    # Re-enable the IRQ with the rising edge trigger for the next button press
    pin.irq(trigger=Pin.IRQ_RISING, handler=button_pressed_handler)


def button_pressed_handler_debounce(pin):
    """
    This handler is a more advanced version with a time-based debounce mechanism.
    It checks the time between presses and only counts a press if it is more
    than 200 ms since the last press.
    """
    global button_presses, last_time
    new_time = time.ticks_ms()  # Get the current time in milliseconds
    # If it has been more than 200 ms since the last press, count the press
    if (new_time - last_time) > 200:
        button_presses += 1  # Increment the press count
        last_time = new_time  # Update the last_time to the current time


def main():
    """
    Main function to initialize the GPIO pin, set up the interrupt request (IRQ)
    handler for the button press, and handle the printing of the button press count.
    """
    led: Pin = Pin(16, Pin.OUT)  # Set up an LED on GPIO pin 16 as an output
    # Initialize the button pin on GPIO pin 34 as an input with a pull-down resistor
    switch_pin: Pin = Pin(34, Pin.IN, Pin.PULL_DOWN)

    # Register the handler function for button presses (IRQ on rising edge)
    switch_pin.irq(trigger=Pin.IRQ_RISING, handler=button_pressed_handler)

    # Variable to track the last printed press count value to avoid redundant prints
    old_presses: int = 0
    while True:
        # Print the button press count only when it changes
        if button_presses != old_presses:
            print(button_presses)  # Print the current button press count
            led.value(not led.value())  # Toggle the LED to indicate a press
            old_presses = button_presses  # Update the old_presses variable


# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
