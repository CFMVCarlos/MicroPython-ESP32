import _thread
import time

# Define a global variable to signal threads to stop
stop_threads = False

# Create a lock object
lock = _thread.allocate_lock()


# Define a function to be executed in a separate thread
def thread_function(thread_id, delay):
    global stop_threads
    print("Thread ID:", _thread.get_ident())
    while not stop_threads:
        lock.acquire()
        print("Thread", thread_id, "is running")
        lock.release()
        time.sleep(delay)
    print("Thread", thread_id, "stopped")


# Create two threads
try:
    _thread.start_new_thread(
        thread_function, (1, 1)
    )  # Thread ID 1, with a delay of 1 second
    _thread.start_new_thread(
        thread_function, (2, 2)
    )  # Thread ID 2, with a delay of 2 seconds

except Exception as e:
    print("Error: unable to start thread:", e)

# Main thread continues to execute
try:
    while True:
        pass  # Do nothing, main thread continues to run
except KeyboardInterrupt:
    print("Ctrl+C pressed. Stopping all threads.")
    stop_threads = True  # Signal threads to stop
