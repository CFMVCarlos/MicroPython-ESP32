import array
import struct

# @ - native byte order, standard size and alignment
# < - little-endian byte order
# > - big-endian byte order
# ! - network byte order

# b - signed char - integer - 1 byte
# B - unsigned char - integer - 1 byte
# h - short - integer - 2 bytes
# H - unsigned short - integer - 2 bytes
# i - int - integer - 4 bytes
# I - unsigned int - integer - 4 bytes
# l - long - integer - 4 bytes
# L - unsigned long - integer - 4 bytes
# q - long long - integer - 8 bytes
# Q - unsigned long long - integer - 8 bytes
# e - half float - float - 2 bytes
# f - float - float - 4 bytes
# d - double - float - 8 bytes
# s - char[] - bytes
# p - void * - integer

# Calculate the size needed to store the format '<HH'
size = struct.calcsize("<HH")
print("Size of '<HH':", size)  # Output: Size of '<HH': 4

# Pack the values 10, 20 into the format '<HH'
packed_data = struct.pack("<HH", 10, 20)
print("Packed data:", packed_data)  # Output: Packed data: b'\n\x00\x14\x00'

# Pack the values 10, 20 into the format '>HH'
packed_data = struct.pack(">HH", 10, 20)
print("Packed data:", packed_data)  # Output: Packed data: b'\x00\n\x00\x14'

# Create a byte buffer using array
buffer = array.array("B", [0] * 4)

# Pack values 10, 20 into the format '<HH' into buffer starting at offset 0
struct.pack_into("<HH", buffer, 0, 10, 20)
print("Packed buffer:", buffer)  # Output: Packed buffer: array('B', [10, 0, 20, 0])

# Unpack the data b'\n\x00\x14\x00' into values using the format '<HH'
unpacked_values = struct.unpack("<HH", b"\n\x00\x14\x00\x1e\x00")
print("Unpacked values:", unpacked_values)  # Output: Unpacked values: (10, 20)

# Unpack the data b'\n\x00\x14\x00' starting at offset 0 into values using the format '<HH'
unpacked_values = struct.unpack_from("<HH", b"\n\x00\x14\x00\x1e\x00", 2)
print("Unpacked values:", unpacked_values)  # Output: Unpacked values: (10, 20)
