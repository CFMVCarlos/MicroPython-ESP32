import sys

# sys.exit(retval=0)
try:
    sys.exit(1)
except SystemExit as e:
    print("Exited with code:", e)

# sys.print_exception(exc, file=sys.stdout)
try:
    x = 1 / 0
except Exception as e:
    print("\nSystem Print Exception:")
    sys.print_exception(e)
    print()

# Constants:

# sys.argv
print("Arguments:", sys.argv)

# sys.byteorder
print("Byte order:", sys.byteorder)

# sys.implementation
print("Implementation name:", sys.implementation.name)
print("Implementation version:", sys.implementation.version)

# sys.maxsize
print("Maximum size:", sys.maxsize)

# sys.modules
print("Loaded modules:", sys.modules)

# sys.path
print("Module search path:", sys.path)

# sys.platform
print("Platform:", sys.platform)

# sys.ps1 and sys.ps2
sys.ps1 = ">>>>>> "
sys.ps2 = "...... "

# sys.stderr, sys.stdin, sys.stdout
sys.stderr.write("Error message\n")
sys.stdout.write("Output message\n")

# sys.version and sys.version_info
print("Python version:", sys.version)
print("Python version info:", sys.version_info)
