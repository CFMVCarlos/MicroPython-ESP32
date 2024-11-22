# This function demonstrates different types of parameters in Python:
# - Positional-only parameters
# - Regular parameters
# - Keyword-only parameters
def example_function(
    positional1="Default Value 1",  # Positional-only parameter with a default value
    positional2="Default Value 2",  # Positional-only parameter with a default value
    positional3="Default Value 3",  # Positional-only parameter with a default value
    /,  # This marks the end of the positional-only parameters
    parameter1="Default Value 1",  # Regular parameter with a default value
    parameter2="Default Value 2",  # Regular parameter with a default value
    parameter3="Default Value 3",  # Regular parameter with a default value
    *,  # This marks the start of the keyword-only parameters
    keyword1="Default Value 1",  # Keyword-only parameter with a default value
    keyword2="Default Value 2",  # Keyword-only parameter with a default value
    keyword3="Default Value 3",  # Keyword-only parameter with a default value
) -> None:
    # Print the positional-only parameters
    print("Positional Only parameter 1:", positional1)
    print("Positional Only parameter 2:", positional2)
    print("Positional Only parameter 3:", positional3)

    # Print the regular parameters
    print("Parameter 1:", parameter1)
    print("Parameter 2:", parameter2)
    print("Parameter 3:", parameter3)

    # Print the keyword-only parameters
    print("Keyword Only parameter 1:", keyword1)
    print("Keyword Only parameter 2:", keyword2)
    print("Keyword Only parameter 3:", keyword3)


# Function to join multiple strings together with a separator
def join_text(*strings, sep=" "):
    # Return the joined strings with the specified separator
    return sep.join(strings)


# Example usage of the example_function with positional and keyword arguments
example_function(
    "Positional Value 1",  # Positional argument for positional1
    "Positional Value 2",  # Positional argument for positional2
    "Positional Value 3",  # Positional argument for positional3
    "Parameter Value 4",  # Regular argument for parameter1
    parameter2="Parameter Value 5",  # Keyword argument for parameter2
    keyword1="Keyword Value 7",  # Keyword argument for keyword1
    keyword2="Keyword Value 8",  # Keyword argument for keyword2
)

# Demonstrating the join_text function with different separators
print(join_text("A", "B", sep="-"))  # Joins "A" and "B" with a dash separator
print(
    join_text("A", "B", "C", "D", sep="-")
)  # Joins "A", "B", "C", and "D" with a dash separator
print(
    join_text("A", "B", "C", "D", sep="*")
)  # Joins "A", "B", "C", and "D" with an asterisk separator
print(join_text("A", "B", "C", "D", "E", "F", sep="/"))  # Joins with a slash separator
