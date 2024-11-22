import machine

# Initialize the RTC object
rtc = machine.RTC()

# Set the date and time
rtc.datetime((2023, 4, 1, 3, 12, 30, 0, 0))

# Get the current date and time
current_datetime = rtc.datetime()
print("Current date and time:", current_datetime)

# Initialize the RTC with a specific datetime
rtc.init((2023, 4, 1, 3, 12, 30, 0, 0))

# Write data to RTC memory
data_to_write = b"Hello RTC Memory!"
rtc.memory(data_to_write)

# Read data from RTC memory
data_read = rtc.memory()
print("Data read from RTC memory:", data_read)
