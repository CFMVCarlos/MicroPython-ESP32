# Import time-related functions for delay and tick counting
from time import sleep, ticks_diff, ticks_ms, ticks_us
import network  # Import network module to interact with WiFi
import requests  # Import requests module to make HTTP requests
import secrets_network as secrets_network  # Import a secrets file containing WiFi credentials


def main():
    """
    Main function that connects to a WiFi network, fetches data from a public API,
    and retrieves the MAC address of the device.
    """
    # Print the WiFi network name being connected to
    print("Connecting to WiFi Network Name:", secrets_network.SSID)

    # Initialize the WiFi object in station mode (STA_IF)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)  # Activate the WiFi interface

    start = ticks_ms()  # Start a millisecond counter to measure connection time

    # If the device is not already connected to WiFi, attempt to connect
    if not wlan.isconnected():
        wlan.connect(
            secrets_network.SSID, secrets_network.PASSWORD
        )  # Connect to the WiFi
        print("Waiting for connection...")  # Print status while waiting
        counter = 0  # Initialize a counter to track connection attempts

        # Loop while waiting for the connection
        while not wlan.isconnected():
            sleep(1)  # Wait for 1 second before trying again
            print(".", sep="", end="")  # Print a dot to show progress
            counter += 1
            if counter > 20:  # If the device has tried for too long, stop trying
                print("Connection failed!")
                break
        else:
            # Once connected, calculate and display the time taken to connect
            delta = ticks_diff(ticks_ms(), start)
            print("\nConnect Time:", delta, "milliseconds")
            print("IP Address:", wlan.ifconfig()[0])  # Print the assigned IP address
    else:
        print(
            "IP Address:", wlan.ifconfig()[0]
        )  # If already connected, just print the IP address

    # If connected to the network, fetch data from a public API
    if wlan.isconnected():
        print()  # Print a newline for better readability

        start = ticks_ms()  # Start a millisecond counter to measure HTTP request time

        # Fetch data from the Open Notify API to get the list of astronauts in space
        astronauts = requests.get("http://api.open-notify.org/astros.json").json()

        delta = ticks_diff(
            ticks_ms(), start
        )  # Calculate the time taken for the HTTP request

        # Extract and print the number of astronauts currently in space
        number = astronauts["number"]
        print("There are", number, "astronauts in space.")
        # Print the names of the astronauts
        for i in range(number):
            print(i + 1, astronauts["people"][i]["name"])

        # Print the time taken for the HTTP GET request in milliseconds
        print("HTTP GET Time in milliseconds:", delta)
        print()

        ####################################################################################################################

        # Start a microsecond counter to measure the time taken to fetch the MAC address
        start = ticks_us()

        # Retrieve the MAC address of the device
        mac_address = wlan.config("mac")

        # Print the time taken to fetch the MAC address in microseconds
        print("Time in microseconds:", ticks_diff(ticks_us(), start))

        # Print the MAC address in raw byte format
        print("Hex byte array:", mac_address, "length:", len(mac_address))

        # Print the MAC address in standard MAC address notation (xx:xx:xx:xx:xx:xx)
        # Loop through the first five bytes and print them in hexadecimal format
        for digit in range(0, 5):
            print(str(hex(mac_address[digit]))[2:4], ":", sep="", end="")

        # Print the last byte of the MAC address without a colon at the end
        print(str(hex(mac_address[5]))[2:4])


if __name__ == "__main__":
    main()  # Run the main function when the script is executed
