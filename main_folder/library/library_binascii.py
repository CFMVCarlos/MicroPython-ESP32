import binascii

# Binary data
binary_data = b"Hello, World!"

# Convert binary data to ASCII hex representation
hex_representation = binascii.hexlify(binary_data)
print("Hex representation:", hex_representation)

# Convert ASCII hex representation back to binary data
decoded_data = binascii.unhexlify(hex_representation)
print("Decoded data:", decoded_data.decode())

# Encode ASCII string to Base64
encoded_base64 = binascii.b2a_base64(binary_data)
print("Encoded Base64:", encoded_base64)

# Decode Base64 to binary
decoded_binary = binascii.a2b_base64(encoded_base64)
print("Decoded Binary:", decoded_binary.decode())
