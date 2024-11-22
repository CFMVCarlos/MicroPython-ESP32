import time

import micropython

# micropython.const(expr)
# Use this function to declare a constant value that will be evaluated at compile time.
CONST_X = micropython.const(123)
print("CONST_X:", CONST_X)
CONST_Y = micropython.const(2 * CONST_X + 1)
print("CONST_Y:", CONST_Y)

# micropython.opt_level([level])
# Set the optimization level for the bytecode compiler.
# Assertions: at level 0 assertion statements are enabled and compiled into the bytecode; at levels 1 and higher assertions are not compiled.
# Built-in __debug__ variable: at level 0 this variable expands to True; at levels 1 and higher it expands to False.
# Source-code line numbers: at levels 0, 1 and 2 source-code line number are stored along with the bytecode so that exceptions can report the line number they occurred at;
# at levels 3 and higher line numbers are not stored.
micropython.opt_level(1)
print("Optimization level:", micropython.opt_level())

# micropython.alloc_emergency_exception_buf(size)
# Allocate a buffer for the emergency exception handler.
# This buffer is used to catch stack overflows and other exceptions that would otherwise cause a crash.
print()
micropython.alloc_emergency_exception_buf(100)
print()

# micropython.mem_info([verbose])
# Print information about the memory usage.
micropython.mem_info(True)
print()

# micropython.qstr_info([verbose])
# Print information about the qstrings (interned strings) usage.
micropython.qstr_info(True)
print()

# micropython.stack_use()
print("Stack usage:", micropython.stack_use())

# micropython.kbd_intr(chr)
micropython.kbd_intr(3)  # Set Ctrl-C to raise KeyboardInterrupt
time.sleep(1)
micropython.kbd_intr(-1)  # Disable capture of Ctrl-C


# micropython.schedule(func, arg)
def scheduled_func(arg):
    print("Scheduled function called with arg:", arg)


# Schedule the function func to be executed “very soon” in the main thread.
micropython.schedule(scheduled_func, "Hello")

print("End of script")
