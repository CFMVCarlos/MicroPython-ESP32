import time

from machine import PWM, Pin

pin = Pin(16, Pin.OUT, Pin.PULL_DOWN)  # create output pin on GPIO0
pwm = PWM(pin, freq=1000)  # create a PWM object on a pin and set freq

pwm.duty_u16(int(65535 / 2))  # set duty to 50% (duty_u16 / 65535)
time.sleep(1)

MAX_DUTY: int = 2**16 - 1
for duty in range(MAX_DUTY):
    pwm.duty_u16(duty)
    time.sleep_us(10)
for duty in range(MAX_DUTY, 0, -1):
    pwm.duty_u16(duty)
    time.sleep_us(10)

pwm.deinit()
