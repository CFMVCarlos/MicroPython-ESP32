import random

random.seed(10)  # Seed the random number generator

# Functions for integers
print("Random bits:", bin(random.getrandbits(4)))
print("Random integer in range [1, 10]:", random.randint(1, 10))
print("Random integer in range [0, 10) (step=2):", random.randrange(0, 10, 2))

# Functions for floats
print("Random floating point number between [0.0, 1.0):", random.random())
print("Random floating point number between [1.0, 5.0]:", random.uniform(1.0, 5.0))

# Other functions
print("Random choice from a list:", random.choice([1, 2, 3, 4, 5]))
