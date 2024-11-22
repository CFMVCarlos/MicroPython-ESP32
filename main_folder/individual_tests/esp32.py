from math import e

import esp
import esp32
import machine
import network
import utime
from machine import (
    DAC,
    I2C,
    PWM,
    RTC,
    SPI,
    UART,
    WDT,
    Pin,
    SoftI2C,
    SoftSPI,
    Timer,
    TouchPad,
)

# Import network secrets for Wi-Fi connection
import main_folder.secrets_network as secrets_network

# Display machine-related information
print("-----Machine-----")
print(f"Machine Frequency: {machine.freq()} Hz")  # Print current CPU frequency
machine.freq(240000000)  # Set the CPU frequency to 240 MHz for improved performance

# Display ESP-related information
print("-----ESP-----")
print(f"Flash Size: {esp.flash_size()} bytes")  # Print flash size of ESP module

# Display ESP32-specific information
print("-----ESP32-----")
temp_fahrenheit: int = (
    esp32.raw_temperature()
)  # Get the internal temperature of the MCU in Fahrenheit
temp_celsius: float = (temp_fahrenheit - 32.0) / 1.8  # Convert to Celsius
print(f"Temperature = {temp_fahrenheit:4d} deg F or {temp_celsius:5.1f} deg C")
esp32.ULP()  # Access the Ultra-Low-Power Co-Processor for low power tasks

# Network setup and display network-related information
print("-----Network-----")
wlan = network.WLAN(network.STA_IF)  # Create station interface for Wi-Fi connection
wlan.active(True)  # Activate the Wi-Fi interface
print(wlan.scan())  # Scan for available Wi-Fi access points
print(wlan.isconnected())  # Check if the station is already connected
wlan.connect(
    secrets_network.SSID, secrets_network.PASSWORD
)  # Connect to a known Wi-Fi network using SSID and password
print(wlan.config("mac"))  # Print MAC address of the station
print(wlan.ifconfig())  # Print IP, netmask, gateway, and DNS addresses of the station

# Create and configure an access point (AP) interface
ap = network.WLAN(network.AP_IF)  # Create access-point interface
ap.active(True)  # Activate the AP interface
ap.config(ssid="ESP-AP")  # Set the SSID for the access point
ap.config(max_clients=10)  # Limit the number of clients that can connect to the AP

# Time-related operations using the uTime library
print("-----uTime-----")
utime.sleep(1)  # Sleep for 1 second
utime.sleep_ms(500)  # Sleep for 500 milliseconds
utime.sleep_us(10)  # Sleep for 10 microseconds
start = utime.ticks_ms()  # Capture the current time in milliseconds
delta = utime.ticks_diff(utime.ticks_ms(), start)  # Calculate time difference

# Setup and use machine timers
print("-----Machine Timer-----")
tim0 = Timer(0)  # Create timer 0
tim0.init(
    period=5000, mode=Timer.ONE_SHOT, callback=lambda t: print(0)
)  # Initialize timer 0 to fire once after 5000 ms
tim1 = Timer(1)  # Create timer 1
tim1.init(
    period=2000, mode=Timer.PERIODIC, callback=lambda t: print(1)
)  # Initialize timer 1 to fire periodically every 2000 ms

# GPIO Pin configuration
print("-----Pin-----")
# Configure a pin with specific settings (output, pull-up, drive strength, and initial value)
p16 = Pin(16, Pin.OUT, Pin.PULL_UP, drive=Pin.DRIVE_3, value=1)

# UART communication setup
print("-----UART-----")
uart1 = UART(
    1, baudrate=9600, tx=33, rx=32
)  # Initialize UART1 with TX on pin 33 and RX on pin 32
uart1.write("hello")  # Send a message via UART
uart1.read(5)  # Read up to 5 bytes from UART

# PWM signal generation and configuration
print("-----PWM-----")
pwm0 = PWM(
    Pin(0), freq=5000, duty_u16=32768
)  # Create PWM on pin 0 with a frequency of 5 kHz
print(pwm0.freq())  # Get the current PWM frequency
pwm0.freq(1000)  # Set PWM frequency to 1 kHz
print(pwm0.duty())  # Get current duty cycle (0-1023)
pwm0.duty(256)  # Set duty cycle to 25% (256/1023)
pwm0.duty_u16(2**16 * 3 // 4)  # Set duty cycle to 75% (using 16-bit duty cycle)
print(pwm0.duty_ns())  # Get pulse width in nanoseconds
pwm0.duty_ns(250_000)  # Set pulse width to 250 microseconds
pwm0.deinit()  # Deinitialize PWM to stop output

# DAC (Digital-to-Analog Conversion) configuration
print("-----DAC-----")
dac = DAC(Pin(25))  # Initialize DAC on pin 25
dac.write(128)  # Output a 50% voltage (128/255)

# SoftSPI setup (Software-based SPI communication)
print("-----SoftSPI-----")
spi = SoftSPI(
    baudrate=100000, polarity=1, phase=0, sck=Pin(0), mosi=Pin(2), miso=Pin(4)
)  # SoftSPI bus on specific pins
spi.init(baudrate=200000)  # Set SoftSPI baud rate
print(spi.read(10))  # Read 10 bytes from SPI
print(spi.read(10, 0xFF))  # Read 10 bytes, outputting 0xFF on MOSI
spi.write(b"12345")  # Write data to SPI
spi.write_readinto(b"1234", bytearray(4))  # Write and read simultaneously

# SPI hardware interface configuration
print("-----SPI-----")
hspi = SPI(
    1, 10000000, sck=Pin(14), mosi=Pin(13), miso=Pin(12)
)  # Hardware SPI on specific pins

# SoftI2C setup (Software-based I2C communication)
print("-----SoftI2C-----")
i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=100000)  # SoftI2C bus on specific pins
print(i2c.scan())  # Scan for I2C devices

# I2C hardware interface setup
print("-----I2C-----")
i2c = I2C(
    1, scl=Pin(5), sda=Pin(4), freq=400000
)  # Hardware I2C with specific pins and frequency

# Real-time Clock (RTC) configuration
print("-----RTC-----")
rtc = RTC()  # Create RTC object
rtc.datetime((2017, 8, 23, 1, 12, 48, 0, 0))  # Set a specific date and time
print(rtc.datetime())  # Print current date and time from RTC

# Watchdog Timer (WDT) setup
print("-----WDT-----")
wdt = WDT(timeout=5000)  # Initialize Watchdog Timer with a 5-second timeout
wdt.feed()  # Feed the watchdog to prevent reset

# Touchpad sensor setup
print("-----TouchPad-----")
t = TouchPad(Pin(14))  # Initialize TouchPad on pin 14
t.config(500)  # Set touch detection threshold
esp32.wake_on_touch(True)  # Enable wake on touch event
machine.lightsleep()  # Put the device into light sleep mode
print(t.read())  # Read the touchpad value (smaller number indicates a touch)

# Main loop for continuous operations
try:
    while True:
        utime.sleep_ms(10)  # Sleep for 10 ms
except KeyboardInterrupt:
    # Handle clean-up on keyboard interrupt
    tim0.deinit()
    tim1.deinit()
    print("Timers 0 and 1 deinitialized")
    ap.active(False)
    wlan.active(False)
    print("Access Point and WLAN deactivated")
    machine.freq(80000000)  # Reset the machine frequency to 80 MHz
    print("Machine Frequency set to 80 MHz")
    print("Done")
except Exception as e:
    # Handle unexpected errors
    print("An error occurred:", e)
