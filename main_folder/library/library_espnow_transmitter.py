import espnow
import network

try:
    # A WLAN interface must be active to send()/recv()
    sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
    sta.active(True)
    print(f'MAC Address: {network.WLAN().config("mac")}')

    e = espnow.ESPNow()
    e.config(
        rxbuf=526, timeout_ms=300_000
    )  # Set buffer size and timeout (ms) to the default values
    e.active(True)

    # Define your PMK as a byte string
    pmk = b"\x01\x23\x45\x67\x89\xAB\xCD\xEF\xFE\xDC\xBA\x98\x76\x54\x32\x10"
    e.set_pmk(pmk)  # Set the PMK

    # Define the Local Master Key (LMK) for encryption
    lmk = b"\x01\x23\x45\x67\x89\xAB\xCD\xEF\xFE\xDC\xBA\x98\x76\x54\x32\x10"
    peer_mac = b"\xc4[\xbe\x17\xbe\x0c"  # MAC address of peer's wifi interface
    e.add_peer(peer_mac, lmk=lmk)  # Must add_peer() before send()

    print("Sending messages...")
    e.send("Starting...")
    for i in range(10):
        e.send(None, str(i) * 10, True)
    e.send("end")

    print("Sending messages to be received using irecv()...")
    e.send("Starting...")
    for i in range(10):
        e.send(None, str(i) * 10, True)
    e.send("end")

    print("Sending messages to be received using interrupts...")
    e.send("Starting...")
    for i in range(10):
        e.send(None, str(i) * 10, True)
    e.send("end")

    try:
        e.send("Hello")
    except OSError as err:
        if len(err.args) < 2:
            raise err
        if err.args[1] == "ESP_ERR_ESPNOW_NOT_INIT":
            e.active(True)
        elif err.args[1] == "ESP_ERR_ESPNOW_NOT_FOUND":
            e.add_peer(peer_mac)
        elif err.args[1] == "ESP_ERR_ESPNOW_IF":
            network.WLAN(network.STA_IF).active(True)
        else:
            raise err

    # Print the peers table which contains the MAC addresses, RSSI and time the message was received
    print(f"Peers Table: {e.peers_table}")

    bcast = b"\xff" * 6
    e.add_peer(bcast)
    e.send(bcast, "Hello World!")

    print("Done.")
except OSError as error:
    print(f"Error: {error}")
finally:
    print(f"Stats: {e.stats()}")
    e.active(False)
