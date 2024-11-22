import time

import machine
from micropython import const

GPIO_OUT_REG = const(0x3FF44004)  # GPIO 0-31 output register
GPIO_OUT1_REG = const(0x3FF44010)  # GPIO 32-39 output register

GPIO_ENABLE_REG = const(0x3FF44020)  # GPIO 0-31 output enable register
GPIO_ENABLE1_REG = const(0x3FF4402C)  # GPIO 32-39 output enable register

M0 = 1 << 0  # Pin(0) bit mask
M16 = 1 << 16  # Pin(16) bit mask

M32 = 1 << (32 - 32)  # Pin(32) bit mask
M33 = 1 << (33 - 32)  # Pin(33) bit mask

# Enable pin output mode like
# p16 = Pin(16, mode=Pin.OUT)
# p17 = Pin(17, mode=Pin.OUT)
# p32 = Pin(32, mode=Pin.OUT)
# p33 = Pin(33, mode=Pin.OUT)
machine.mem32[GPIO_ENABLE_REG] = machine.mem32[GPIO_ENABLE_REG] | M0 | M16
machine.mem32[GPIO_ENABLE1_REG] = machine.mem32[GPIO_ENABLE1_REG] | M32 | M33

print(hex(machine.mem32[GPIO_OUT_REG]), hex(machine.mem32[GPIO_OUT1_REG]))

# Set outputs to 1 like
# p16(1)
# p17(1)
# p32(1)
# p33(1)
machine.mem32[GPIO_OUT_REG] = machine.mem32[GPIO_OUT_REG] | M0 | M16
machine.mem32[GPIO_OUT1_REG] = machine.mem32[GPIO_OUT1_REG] | M32 | M33

print(hex(machine.mem32[GPIO_OUT_REG]), hex(machine.mem32[GPIO_OUT1_REG]))

time.sleep(2)

# Set outputs to 0 like
# p16(0)
# p17(0)
# p32(0)
# p33(0)
machine.mem32[GPIO_OUT_REG] = machine.mem32[GPIO_OUT_REG] & ~(M0 | M16)
machine.mem32[GPIO_OUT1_REG] = machine.mem32[GPIO_OUT1_REG] & ~(M32 | M33)

print(hex(machine.mem32[GPIO_OUT_REG]), hex(machine.mem32[GPIO_OUT1_REG]))

print()
######################################################

# Reset related functions example
print("Reset cause:", machine.reset_cause())

# Disable interrupts
irq_state = machine.disable_irq()

# Perform time-critical work here

# Enable interrupts
machine.enable_irq(irq_state)

# Get CPU frequency
print("CPU frequency:", machine.freq())

# Enter lightsleep mode for 1 second
print("Entering lightsleep mode for 1 second...")
machine.lightsleep(1000)

# Get wake reason
# After waking up from deep sleep, print the wake-up reason
wake_reason = machine.reset_cause()

if wake_reason == machine.DEEPSLEEP_RESET:
    print("Woke up from deep sleep.")
elif wake_reason == machine.PWRON_RESET:
    print("Woke up from power-on reset.")
elif wake_reason == machine.HARD_RESET:
    print("Woke up from hard reset.")
elif wake_reason == machine.WDT_RESET:
    print("Woke up from watchdog timer reset.")
elif wake_reason == machine.SOFT_RESET:
    print("Woke up from soft reset.")
elif wake_reason == machine.WLAN_WAKE:
    print("Woke up from WLAN wake.")
elif wake_reason == machine.PIN_WAKE:
    print("Woke up from pin wake.")
elif wake_reason == machine.RTC_WAKE:
    print("Woke up from RTC wake.")
else:
    print("Unknown wake-up reason:", wake_reason)

# Get unique identifier
unique_id = machine.unique_id()
print("Unique ID:", unique_id)

# Time a pulse on pin 0
duration = machine.time_pulse_us(0, 1)
print("Pulse duration on pin 0 (us):", duration)

# Transmit data using bitstream
machine.bitstream(16, 0, (400, 850, 800, 450), b"\x01")

# Enter deep sleep mode for 2 seconds
machine.deepsleep(2000)
