# MicroPython-ESP32

This repository contains a set of test scripts and examples for running on the ESP32 board using MicroPython. The tests cover a variety of microcontroller features such as PWM, GPIO interrupts, ADC, timers, and WiFi network interactions.

### Setup (Optional)

Before running the scripts, you can optionally install `mpy-cross`, a tool used to compile Python files into MicroPython bytecode (`.mpy`). While using `mpy-cross` can improve the performance of your scripts on the ESP32, it is not required to run the tests. The scripts will work with standard Python files (`.py`) as well.

To install `mpy-cross`, run:

```bash
pip install mpy-cross
```

Once installed, you can use it to compile Python files into bytecode with the following command:

```bash
mpy-cross <file>.py
```

This generates a `.mpy` file, which is more efficient for execution on the ESP32. 

**Why use `mpy-cross`?**
Using `mpy-cross` compiles Python files into bytecode, which can improve performance, reduce memory usage, and speed up execution. However, it's not mandatory, and you can still run the `.py` files directly on the ESP32 if you prefer.

### Uploading Files to ESP32

The `upload.cmd` script automatically transfers files in the current directory to the ESP32 board using `mpremote.py`. This simplifies the process of transferring code to the device, especially when dealing with multiple files.

To upload files to the ESP32, run:

```bash
upload.cmd
```

### Individual Tests

`main.py` is used to select which individual test script to run. The available tests are:

#### PWM
This script initializes a Pulse Width Modulation (PWM) signal on Pin 16 with a frequency of 1 kHz and 16-bit resolution, using the PWM and Pin classes from the `machine` module. The duty cycle of the PWM signal gradually increases from 0 to its maximum value (65535) and then decreases back to 0 in an infinite loop. A 100-microsecond delay is applied between each adjustment to the duty cycle. The program continues running until interrupted (e.g., by pressing CTRL+C), at which point the PWM is deinitialized and the resources are released.

#### GPIO Interrupt
This script implements a button press counter with debounce handling. It uses the `machine` and `time` modules to set up an interrupt request (IRQ) on GPIO pin 34. Each button press increments a counter, and an LED connected to GPIO pin 16 is toggled each time the button press count changes. The script uses two debounce mechanisms: one with a simple 200ms delay and another that tracks the time between presses to ensure multiple rapid presses aren't counted. The updated press count is printed to the terminal. The program continuously runs, efficiently handling button presses and printing the updated count.

#### ADC (Analog-to-Digital Conversion)
This script reads analog values from a voltage divider connected to GPIO pin 13. It uses the `ADC` class from the `machine` module to set the ADC attenuation to 11dB, allowing readings of higher voltage ranges. The script continuously reads the raw ADC value, converts it to voltage (in microvolts), and prints both the raw ADC value and the corresponding voltage. A 250ms delay is introduced between readings to control the update frequency. This setup is useful for monitoring analog voltage levels from sensors in real-time.

#### Timer
This script demonstrates the use of timers and GPIO control. It initializes an LED on GPIO pin 16 and uses two timers: a periodic timer that toggles the LED every second, and a one-shot timer that triggers a callback function after 10 seconds. The `tick` function toggles the LED state every time the periodic timer is triggered. The `timer_callback` function prints a message after the one-shot timer expires. The main function manages both timers and handles cleanup when the program is interrupted. This setup is ideal for applications requiring periodic events and timed actions, such as LED blinking or timeouts.

#### WiFi Network
This script connects the device to a WiFi network, fetches data from a public API, and retrieves the device's MAC address. It uses credentials stored in the `secrets_network` file to connect to the WiFi. Once connected, the script prints the connection time and the assigned IP address. It then makes an HTTP GET request to the Open Notify API to fetch the number of astronauts currently in space, printing their names and the request time. Finally, it retrieves and prints the MAC address of the device, measuring the time taken for this operation in microseconds. This is useful for network-based applications and device identification.

### Library Scripts

The library scripts are not implemented in the `main.py` file but can be run directly on the microcontroller using the REPL (Read-Eval-Print Loop). These scripts serve as references for future projects, containing functions for each of the libraries integrated into MicroPython. You can access these functions and libraries directly on the ESP32 and experiment with them for custom use cases.

## Binary Files

Each binary file in the `micropython_bin_files` folder is accompanied by a command-line script designed to streamline the flashing process for the ESP32. These scripts perform the following actions:

1. **Erase Flash**: Completely clears the ESP32's flash memory to ensure a clean installation.
2. **Flash Binary**: Writes the specified binary file to the ESP32 using `esptool.py`.
3. **Reset ESP32**: Automatically restarts the ESP32 after the flashing process, ensuring the new firmware is correctly loaded.

These scripts simplify the workflow, allowing you to quickly and reliably prepare your ESP32 for use with the desired MicroPython firmware.

## Author

- [Carlos Valente](https://github.com/CFMVCarlos)