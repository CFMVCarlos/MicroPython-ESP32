# Import necessary modules for microcontroller operations
import machine
import micropython

# Allocate emergency exception buffer to help with debugging
micropython.alloc_emergency_exception_buf(100)


class Foo(object):
    """
    Class Foo controls an LED on a specified GPIO pin and manages a timer.
    The LED toggles every specified period, and a count is tracked.
    """

    def __init__(self, timer_number: int, timer_freq: int, board_pin: int):
        """
        Initializes the Foo class with a timer and an LED pin.
        - `timer_number`: The timer number (e.g., 4).
        - `timer_freq`: The frequency of the timer (e.g., 1 Hz).
        - `board_pin`: The GPIO pin number to control the LED (e.g., 16).
        """
        # Initialize the LED pin as an output with a pull-up resistor
        self.led = machine.Pin(board_pin, machine.Pin.OUT, machine.Pin.PULL_UP)
        self._count = 0  # Initialize the count for tracking timer events

        # Initialize the timer with the specified frequency, periodic mode, and callback function
        machine.Timer(timer_number).init(
            freq=timer_freq, mode=machine.Timer.PERIODIC, callback=self.cb
        )

    def cb(self, tim):
        """
        Callback function for the timer interrupt. This function is called every time the timer triggers.
        It toggles the LED state and increments the count.
        """
        self.led.value(not self.led.value())  # Toggle the LED state (on/off)
        self._count += 1  # Increment the count every time the timer triggers

    def get_count(self) -> int:
        """
        Returns the current count value.
        """
        return self._count

    def set_count(self, value) -> None:
        """
        Sets the count value to the specified value.
        This function is used to reset the count or set it to a specific number.
        """
        self._count = value


def main() -> None:
    """
    Main function to create an instance of the Foo class, monitor the count, and print a message when 10 seconds have passed.
    This function runs indefinitely until a KeyboardInterrupt occurs.
    """
    # Create an instance of the Foo class with timer number 4, timer frequency of 1 Hz, and control LED on GPIO pin 16
    red = Foo(timer_number=4, timer_freq=1, board_pin=16)

    try:
        # Run an infinite loop to check the count and print a message every 10 seconds
        while True:
            if (
                red.get_count() == 10
            ):  # Check if 10 seconds have elapsed (count reaches 10)
                print("10 Seconds have elapsed")  # Print a message
                red.set_count(0)  # Reset the count to 0
    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (Ctrl+C) gracefully
        print("KeyboardInterrupt")
        raise SystemExit  # Exit the program


# Start the main function if this script is executed directly
if __name__ == "__main__":
    main()
