# Import ADC class to interact with the analog-to-digital converter
from machine import ADC

# Import sleep function to pause execution in milliseconds
from utime import sleep_ms


def main():
    # Create an ADC object for pin 13 (GPIO 13)
    voltage_divider = ADC(13)

    # Set the ADC attenuation to 11dB (this increases the input range to the ADC, enabling reading higher voltages)
    voltage_divider.atten(ADC.ATTN_11DB)

    # Continuous loop to read ADC values
    while True:
        # Read the 16-bit ADC value (raw value) and convert to voltage (in microvolts)
        raw_adc = voltage_divider.read_u16()
        voltage = voltage_divider.read_uv() * 1e-6  # Convert to voltage (volts)

        # Print the raw ADC value and the corresponding voltage
        print(f"Raw ADC: {raw_adc}, Voltage: {voltage} V")

        # Delay for 250 milliseconds before reading again
        sleep_ms(250)


# Ensure the script runs only when executed directly, not when imported
if __name__ == "__main__":
    main()
