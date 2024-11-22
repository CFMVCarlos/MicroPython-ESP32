import espnow
import network

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)
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
transmitter_mac = b"\xc4[\xbe\x17\xbf\xa8"
e.add_peer(transmitter_mac, lmk=lmk)

print("Waiting for ESPNow messages...")
while True:
    host, msg = e.recv(3000)  # 3 seconds timeout
    if msg:  # msg == None if timeout in recv()
        print(host, msg)
        if msg == b"end":
            break

print("Using irecv to receive messages...")
for mac, msg in e:
    print(mac, msg)
    if msg == bytearray(b"end"):
        break

print("Using interruptions to receive messages...")


def recv_cb(e):
    while True:  # Read out all messages waiting in the buffer
        mac, msg = e.irecv(0)  # Don't wait if no messages left
        if mac is None:
            return
        print(mac, msg)


e.irq(recv_cb)

print(f"Stats: {e.stats()}")
print("Done.")
