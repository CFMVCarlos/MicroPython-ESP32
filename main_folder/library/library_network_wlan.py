from time import sleep, ticks_diff, ticks_ms, ticks_us

import network
import requests

import main_folder.secrets_network as secrets_network

print("Connecting to WiFi Network Name:", secrets_network.SSID)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

start = ticks_ms()  # start a millisecond counter

if not wlan.isconnected():
    wlan.connect(secrets_network.SSID, secrets_network.PASSWORD)
    print("Waiting for connection...")
    counter = 0
    while not wlan.isconnected():
        sleep(1)
        print(".", sep="", end="")
        counter += 1
        if counter > 20:
            print("Connection failed!")
            break
    else:
        delta = ticks_diff(ticks_ms(), start)
        print("\nConnect Time:", delta, "milliseconds")
        print("IP Address:", wlan.ifconfig()[0])
else:
    print("IP Address:", wlan.ifconfig()[0])

if wlan.isconnected():
    print()

    start = ticks_ms()  # start a millisecond counter

    astronauts = requests.get("http://api.open-notify.org/astros.json").json()

    delta = ticks_diff(ticks_ms(), start)

    number = astronauts["number"]
    print("There are", number, "astronauts in space.")
    for i in range(number):
        print(i + 1, astronauts["people"][i]["name"])

    print("HTTP GET Time in milliseconds:", delta)
    print()

    ####################################################################################################################

    start = ticks_us()  # start a millisecond counter
    # This returns a byte array of hex numbers
    mac_address = wlan.config("mac")
    print("Time in microseconds:", ticks_diff(ticks_us(), start))
    # each MAC address is 6 bytes or 48 bits
    print("Hex byte array:", mac_address, "length:", len(mac_address))

    # This should be in hex per the Notational Conventions
    # https://en.wikipedia.org/wiki/MAC_address#Notational_conventions
    # b'(\xcd\xc1\x015X'
    # 28:cd:c1:1:35:58
    # format in MAC Notational Convention
    for digit in range(0, 5):
        print(str(hex(mac_address[digit]))[2:4], ":", sep="", end="")
    print(str(hex(mac_address[5]))[2:4])
