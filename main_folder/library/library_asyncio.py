import asyncio

from machine import Pin


# Asynchronous function to simulate a task
async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)  # Simulate some asynchronous operation
    print(f"Task {name} completed")


# Asynchronous function to wait for multiple tasks with a timeout
async def wait_with_timeout():
    print("Waiting for tasks with a timeout...")
    try:
        await asyncio.wait_for(task("Timeout Task", 5), timeout=3)
    except asyncio.TimeoutError:
        print("Timeout occurred while waiting")


# Asynchronous function to gather tasks and run them in sequence
async def run_tasks_in_sequence():
    print("Running tasks in sequence...")
    await task("Sequential Task 1", 2)
    await task("Sequential Task 2", 1)
    await task("Sequential Task 3", 3)


# Asynchronous function to run multiple tasks concurrently
async def blink(led, period_ms):
    while True:
        led.on()
        await asyncio.sleep_ms(period_ms)
        led.off()
        await asyncio.sleep_ms(period_ms)


async def main(led1, led2):
    # Run tasks concurrently
    await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 1),
        task("Task 3", 3),
        wait_with_timeout(),
        run_tasks_in_sequence(),
    )

    asyncio.create_task(blink(led1, 500))
    asyncio.create_task(blink(led2, 1000))
    await asyncio.sleep_ms(10_000)


asyncio.run(main(Pin(16), Pin(0)))
