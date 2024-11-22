import gc  # Import the garbage collector module to manage memory
import os  # Import the operating system module for interacting with the file system

import machine  # Import the machine module to access hardware-specific functionalities


# Function to return the available disk space in MB
def df():
    # os.statvfs returns filesystem status for the specified path
    s = os.statvfs("//")  # Get filesystem statistics for the root directory
    # Return the available disk space in MB (s[0] is the block size, s[3] is free blocks)
    return "{0} MB".format((s[0] * s[3]) / 1048576)  # Convert bytes to MB


# Function to return the free memory in percentage or detailed info
def free(full=False):
    # gc.mem_free() returns the amount of free memory in bytes
    F = gc.mem_free()
    # gc.mem_alloc() returns the amount of memory allocated in bytes
    A = gc.mem_alloc()
    # Total memory (free + allocated)
    T = F + A
    # Calculate the free memory as a percentage
    P = "{0:.2f}%".format(F / T * 100)
    if not full:
        # If 'full' is False, return just the percentage of free memory
        return P
    else:
        # If 'full' is True, return total memory, free memory, and the free percentage
        return "Total:{0} Free:{1} ({2})".format(T, F, P)


# Function to collect garbage and then return the free memory info
def free_gc(full=False):
    # Run garbage collection to reclaim unused memory
    gc.collect()
    F = gc.mem_free()
    A = gc.mem_alloc()
    T = F + A
    P = "{0:.2f}%".format(F / T * 100)
    if not full:
        return P
    else:
        return "Total:{0} Free:{1} ({2})".format(T, F, P)


# Main function to print system and memory statistics
def main():
    # Print system information (like board name and version)
    print(os.uname())
    # Print available disk space
    print(df())
    # Print free memory percentage
    print(free())
    # Print free memory after garbage collection
    print(free_gc())
    # Print the machine's clock frequency in MHz
    print("Machine Clock Frequency:", "{:,} MHz".format(machine.freq() / 1000000))


# Main function with detailed file system statistics
def main2():
    """
    Print detailed statistics from the virtual file system (vfs)

    The os.statvfs function returns information about the file system for the given path.

    Parameters:
    0 f_bsize – file system block size
    1 f_frsize – fragment size
    2 f_blocks – size of fs in f_frsize units
    3 f_bfree – number of free blocks
    4 f_bavail – number of free blocks for unprivileged users
    5 f_files – number of inodes
    6 f_ffree – number of free inodes
    7 f_favail – number of free inodes for unprivileged users
    8 f_flag – mount flags
    9 f_namemax – maximum filename length
    """

    # Get the file system statistics for the root directory "/"
    stats = os.statvfs("/")
    print(stats)  # Print the raw stats (this is a tuple with all file system details)

    # Extract specific values from the stats tuple
    block_size = stats[0]  # File system block size
    fragment_size = stats[1]  # Fragment size
    total_blocks = stats[2]  # Total number of blocks in the file system

    free_blocks = stats[3]  # Number of free blocks
    available_blocks = stats[4]  # Number of available blocks for unprivileged users

    mount_flags = stats[8]  # Mount flags
    max_filename_length = stats[9]  # Maximum filename length

    # Perform byte calculations to convert block sizes to bytes
    total_bytes = total_blocks * fragment_size
    free_bytes = free_blocks * fragment_size
    available_bytes = available_blocks * fragment_size

    # Print detailed information about the file system
    print("File system block size: {:,} bytes".format(block_size))
    print("Fragment size: {:,} bytes".format(fragment_size))
    print("Size of entire file system in fragment blocks: {:,}".format(total_blocks))
    print("Size of entire file system in bytes: {:,}".format(total_bytes))

    print("Total free blocks for system and users: {:,}".format(free_blocks))
    print(
        "Number of free blocks for unprivileged users: {:,} bytes".format(
            available_blocks
        )
    )

    print("Free size for system and users: {:,} bytes".format(free_bytes))
    print("Free size for users: {:,} bytes".format(available_bytes))
    print("Mount flags: {:,}".format(mount_flags))
    print("Max filename length: {:,}".format(max_filename_length))


# Entry point of the script
if __name__ == "__main__":
    # Call the main functions
    main()
    main2()
