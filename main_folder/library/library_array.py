import array

# b -> unsigned char
# B -> signed char
# h -> signed short
# H -> unsigned short
# i -> signed int
# I -> unsigned int
# l -> signed long
# L -> unsigned long
# q -> signed long long
# Q -> unsigned long long
# f -> float
# d -> double
a = array.array("B", [0x00, 0x16, 0x3E, 0x00, 0x00, 0x00])
print(a)
a.append(0xFF)
print(a)
b = array.array("B", [0x13, 0x14, 0x15])
a.extend(b)
print(a)
