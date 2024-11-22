import time

# time.gmtime([secs]) and time.localtime([secs])
print("UTC time:", time.gmtime())
print("Local time:", time.localtime())

# time.mktime()
local_time_tuple = (
    2024,
    4,
    1,
    12,
    30,
    0,
    3,
    91,
)  # (year, month, day, hour, minute, second, weekday, yearday)
secs_since_epoch = time.mktime(local_time_tuple)
print("Seconds since epoch:", secs_since_epoch)

# time.sleep(seconds)
print("Sleeping for 2 seconds...")
time.sleep(2)
print("Awake!")

# time.sleep_ms(ms)
print("Sleeping for 100 milliseconds...")
time.sleep_ms(100)
print("Awake!")

# time.sleep_us(us)
print("Sleeping for 500 microseconds...")
time.sleep_us(500)
print("Awake!")

# time.ticks_ms(), time.ticks_us(), time.ticks_cpu()
ticks_ms_start = time.ticks_ms()
ticks_us_start = time.ticks_us()

# Do some work...
for i in range(100000):
    pass

ticks_ms_end = time.ticks_ms()
ticks_us_end = time.ticks_us()
# ticks_cpu_end = time.ticks_cpu()

print("Ticks elapsed (ms):", time.ticks_diff(ticks_ms_end, ticks_ms_start))
print("Ticks elapsed (us):", time.ticks_diff(ticks_us_end, ticks_us_start))

# time.ticks_add(ticks, delta)
print("Ticks add example:", time.ticks_add(ticks_ms_start, 500))
# Calculate deadline for operation and test for it
deadline = time.ticks_add(time.ticks_ms(), 1000)
while time.ticks_diff(deadline, time.ticks_ms()) > 0:
    pass
print("Deadline reached")

# Find out TICKS_MAX used by this port
print("TICKS_MAX :", time.ticks_add(0, -1))

# time.time()
print("Time since epoch (s):", time.time())

# time.time_ns()
print("Time since epoch (ns):", time.time_ns())
