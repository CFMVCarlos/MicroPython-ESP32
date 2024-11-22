# Import individual test modules for PWM, GPIO interrupts, ADC, Timer, and WiFi network functionality
from .individual_tests import adc, gpio_interrupt, pwm, timer, wifi_network


def main(choice: int = 0) -> None:
    """
    Main function to execute different test cases based on the user's choice.
    The available tests are:
    - PWM control
    - GPIO interrupt handling
    - ADC (Analog to Digital Conversion)
    - Timer functionality
    - WiFi network interaction

    :param choice: An integer indicating which test to run. Default is 0 (PWM test).
    """
    if choice == 0:
        pwm.main()  # Run the PWM control test
    elif choice == 1:
        gpio_interrupt.main()  # Run the GPIO interrupt test
    elif choice == 2:
        adc.main()  # Run the ADC test
    elif choice == 3:
        timer.main()  # Run the timer functionality test
    elif choice == 4:
        wifi_network.main()  # Run the WiFi network test


if __name__ == "__main__":
    # Set the default choice for the main function (0 = PWM test)
    CHOICE: int = 0
    main(CHOICE)  # Call the main function with the selected choice
