import gc

# Enable automatic garbage collection
gc.enable()

# Allocate some memory
x = [i for i in range(1000)]

# Run a garbage collection
gc.collect()

# Check the number of bytes of heap RAM allocated by Python code
allocated_bytes = gc.mem_alloc()
print("Allocated bytes:", allocated_bytes)

# Check the number of bytes of heap RAM available for Python code to allocate
free_bytes = gc.mem_free()
print("Free bytes:", free_bytes)

# Set a threshold for garbage collection
gc.threshold(10000)  # Trigger collection after every 10,000 bytes allocated

# Allocate more memory to trigger collection
y = [i for i in range(1000)]

# Check the number of bytes of heap RAM allocated by Python code after the threshold
allocated_bytes_after = gc.mem_alloc()
print("Allocated bytes after threshold:", allocated_bytes_after)

# Check the number of bytes of heap RAM available for Python code to allocate after the threshold
free_bytes_after = gc.mem_free()
print("Free bytes after threshold:", free_bytes_after)
