from machine import (
    Pin,
    Timer,
)  # Import necessary classes: Pin for GPIO control and Timer for time-based events
from time import sleep  # Import sleep function to pause the program

# Initialize the LED pin as an output on Pin 16
led = Pin(16, Pin.OUT)


def tick(timer):
    """
    This function toggles the LED state every time the periodic timer triggers.

    :param timer: The timer that triggers the function.
    :return: None
    """
    led.value(
        not led.value()
    )  # Toggle the LED: if it was on, turn it off; if it was off, turn it on


def timer_callback(timer):
    """
    This function prints a message when the one-shot timer reaches 10 seconds.

    :param timer: The timer that triggered the callback.
    :return: None
    """
    print("10 Seconds have elapsed")  # Print message when 10 seconds have passed


def main():
    """
    Main function that initializes timers and manages the periodic LED blinking and
    one-shot timer that triggers after 10 seconds.

    :return: None
    """
    try:
        # Initialize a periodic timer that triggers every second
        tim = Timer(0)
        tim.init(
            freq=1, mode=Timer.PERIODIC, callback=tick
        )  # Timer 0 triggers tick function every second
        print("Timer initialized!")

        # Initialize a one-shot timer that triggers once after 10 seconds
        myOneShotTimer = Timer(1)
        # This timer will trigger the timer_callback function after 10 seconds (10000 ms)
        myOneShotTimer.init(
            mode=Timer.ONE_SHOT,  # Set the timer to one-shot mode
            callback=timer_callback,  # Set the callback function to be called when the timer expires
            period=10000,  # Timer will trigger after 10000 milliseconds (10 seconds)
        )

        while True:
            sleep(0.1)  # Sleep to avoid excessive CPU usage in the main loop

    except KeyboardInterrupt:
        # If the user interrupts the program (Ctrl+C), clean up and deinitialize the timer
        tim.deinit()  # Deinitialize the periodic timer
        print(
            "Timer deinitialized!"
        )  # Print confirmation that the timer was deinitialized


# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function to start the program
