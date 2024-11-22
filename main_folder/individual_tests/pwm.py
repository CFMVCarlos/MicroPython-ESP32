# Import sleep_us function for microsecond delays
from time import sleep_us

# Import PWM (Pulse Width Modulation) and Pin classes from the machine module
from machine import PWM, Pin


def main() -> None:
    """
    This function initializes a PWM object and generates a PWM signal with varying duty cycles.
    It continuously increases and decreases the duty cycle in a loop until interrupted by a keyboard interrupt.

    :return: None
    """
    # Initialize the PWM object on Pin 16 with a frequency of 1000 Hz (1 kHz).
    # Pin is set as an output with a default pull-down resistor.
    pwm: PWM = PWM(Pin(16, Pin.OUT, Pin.PULL_DOWN), freq=1000)
    print("PWM initialized!")  # Print confirmation that PWM is initialized.

    # MAX_DUTY represents the maximum possible duty cycle value for a 16-bit resolution PWM.
    MAX_DUTY: int = 2**16 - 1  # 65535 is the maximum 16-bit value.

    try:
        # Infinite loop to continuously adjust the PWM duty cycle
        while True:
            # Gradually increase the duty cycle from 0 to MAX_DUTY
            for duty in range(MAX_DUTY):
                pwm.duty_u16(
                    duty
                )  # Set the PWM duty cycle to the current value (0-65535)
                sleep_us(
                    100
                )  # Delay for 100 microseconds before updating the duty cycle

            # Gradually decrease the duty cycle from MAX_DUTY back to 0
            for duty in range(MAX_DUTY, 0, -1):
                pwm.duty_u16(duty)  # Set the PWM duty cycle to the current value
                sleep_us(
                    100
                )  # Delay for 100 microseconds before updating the duty cycle
    except KeyboardInterrupt:
        # Handle keyboard interrupt (CTRL+C), which deinitializes the PWM and exits the loop
        pwm.deinit()  # Deinitialize the PWM to release the resources
        print("PWM deinitialized!")  # Print confirmation that PWM is deinitialized


# Entry point of the script to run the main function
if __name__ == "__main__":
    main()  # Call the main function to start the PWM signal generation
