import sys  # Import the sys module, which provides access to system-specific parameters and functions

# Access the _mpy attribute from the sys.implementation object, which contains information about the MicroPython implementation
sys_mpy = sys.implementation._mpy

# Define a list of architecture names corresponding to different MicroPython build targets
arch = [
    None,
    "x86",
    "x64",  # x86 and x64 architectures
    "armv6",
    "armv6m",
    "armv7m",
    "armv7em",
    "armv7emsp",
    "armv7emdp",  # ARM-based architectures
    "xtensa",
    "xtensawin",  # Xtensa architecture (used by ESP32)
][
    sys_mpy >> 10
]  # Use the upper 6 bits of sys_mpy to index into the `arch` list to determine the architecture

# Print the version of the MicroPython interpreter
print(
    "mpy version:", sys_mpy & 0xFF
)  # The lower 8 bits of sys_mpy contain the version number

# Print the sub-version of the MicroPython interpreter
print(
    "mpy sub-version:", sys_mpy >> 8 & 3
)  # The next 2 bits represent the sub-version number

# Print the flags associated with the MicroPython build (architecture-specific)
print("mpy flags:", end="")  # Begin printing the flags

if arch:  # If the architecture is not None (i.e., it's a valid architecture)
    print(" -march=" + arch, end="")  # Print the architecture name (e.g., -march=armv6)

print()  # Print a newline at the end of the output
