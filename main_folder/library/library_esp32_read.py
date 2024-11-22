import esp32

# Create an NVS object providing access to a namespace
nvs = esp32.NVS("my_namespace")

# Get the signed integer value for the specified key
my_int_value = nvs.get_i32("my_int_key")
print("Integer value:", my_int_value)

# Read the value of the blob for the specified key into a buffer
buffer = bytearray(20)  # Allocate a buffer for reading
length_read = nvs.get_blob("my_blob_key", buffer)
print("Blob data read:", buffer[:length_read].decode())
