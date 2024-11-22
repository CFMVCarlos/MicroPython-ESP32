import time

from machine import Pin, Timer

led = Pin(16, Pin.OUT)
led0 = Pin(0, Pin.OUT)


def tick(timer):
    if timer == Timer(0):
        led0.value(not led0.value())
    elif timer == Timer(1):
        led.value(not led.value())
    else:
        print("Unknown timer")


def timer_callback(timer):
    print("10 Seconds have elapsed")


tim = Timer(0)
tim.init(freq=2, mode=Timer.PERIODIC, callback=tick)
print("Timer 1 initialized!")

tim2 = Timer(1)
tim2.init(freq=5, mode=Timer.PERIODIC, callback=tick)
print("Timer 2 initialized!")

myOneShotTimer = Timer(-1)
# call once in 10 seconds from now
myOneShotTimer.init(
    mode=Timer.ONE_SHOT,
    callback=timer_callback,
    period=10000,
)

time.sleep(12)
tim.deinit()
tim2.deinit()
led.off()
