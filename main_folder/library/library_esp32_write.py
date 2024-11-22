import esp32

# Create an NVS object providing access to a namespace
nvs = esp32.NVS("my_namespace")

# Set a 32-bit signed integer value for the specified key
nvs.set_i32("my_int_key", 42)

# Set a binary blob value for the specified key
blob_data = bytearray(b"Hello, NVS!")
nvs.set_blob("my_blob_key", blob_data)

# Erase a key-value pair
nvs.set_i32("my_removed_pair", 42)
nvs.erase_key("my_removed_pair")

# Commit changes made by set_xxx methods to flash
nvs.commit()

print("Data written to NVS successfully.")
