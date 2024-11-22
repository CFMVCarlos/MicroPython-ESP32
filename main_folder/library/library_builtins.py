# abs()
print("Absolute value of -10:", abs(-10))

# all()
print("All elements are True:", all([True, True, True]))
print("All elements are True:", all([True, False, True]))

# any()
print("Any element is True:", any([False, False, True]))
print("Any element is True:", any([False, False, False]))

# bin()
print("Binary representation of 10:", bin(10))

# bool class
print("Boolean value of 0:", bool(0))
print("Boolean value of 1:", bool(1))

# bytearray class
byte_array = bytearray(b"Hello")
print("Byte array:", byte_array)

# bytes class
bytes_data = bytes([65, 66, 67])
print("Bytes:", bytes_data)


# callable()
def func():
    return 42


print("Is func callable?", callable(func))

# chr()
print("Character representation of 97:", chr(97))


# classmethod()
class MyClass:
    @classmethod
    def my_method(cls):
        print("Class method")


MyClass.my_method()

# TODO: compile()
code = 'print("Hello, World!")'
compiled_code = compile(code, "<string>", "exec")
exec(compiled_code)

# complex class
print("Complex number:", complex(3, 4))


# delattr()
class MyClass2:
    attr = 42


delattr(MyClass2, "attr")
print("Attribute deleted:", hasattr(MyClass2, "attr"))

# dict class
my_dict = {"a": 1, "b": 2}
print("Dictionary:", my_dict)

# dir()
print("Directory contents:", dir())

# divmod()
print("Quotient and remainder of 10 divided by 3:", divmod(10, 3))

# enumerate()
print("Enumerated list:", list(enumerate(["a", "b", "c"])))

# eval()
result = eval("2 + 3")
print("Result of expression evaluation:", result)

# TODO: exec()
exec('print("Hello, World!")')


# filter()
def is_even(x):
    return x % 2 == 0


filtered = filter(is_even, [1, 2, 3, 4, 5])
print("Filtered elements:", list(filtered))

# float class
print("Float representation of 3:", float(3))

# frozenset class
frozen_set = frozenset([1, 2, 3])
print("Frozen set:", frozen_set)


# getattr()
class MyClass3:
    attr = 42


obj = MyClass3()
print("Attribute value:", getattr(obj, "attr"))

# globals()
print("Global namespace:", globals())


# hasattr()
class MyClass4:
    attr = 42


obj = MyClass4()
print("Has attribute 'attr'?", hasattr(obj, "attr"))

# hash()
print("Hash of 'hello':", hash("hello"))

# hex()
print("Hex representation of 255:", hex(255))

# id()
print("ID of object:", id(42))

# input()
name = input("Enter your name: ")
print("Hello,", name)

# int class
print("Integer representation of '10':", int("10"))

# isinstance()
print("Is 42 an instance of int?", isinstance(42, int))

# issubclass()
print("Is int a subclass of object?", issubclass(int, object))

# iter()
my_list = [1, 2, 3]
my_iter = iter(my_list)
print("Iterator:", next(my_iter))

# len()
print("Length of list:", len([1, 2, 3]))

# list class
my_list = [1, 2, 3]
print("List:", my_list)

# locals()
print("Local namespace:", locals())


# map()
def double(x):
    return x * 2


result = map(double, [1, 2, 3])
print("Mapped values:", list(result))

# max()
print("Maximum value:", max([1, 2, 3]))

# memoryview class
my_bytes = b"hello"
memory_view = memoryview(my_bytes)
print("Memory view:", memory_view)

# min()
print("Minimum value:", min([1, 2, 3]))

# next()
my_iter = iter([1, 2, 3])
print("Next element:", next(my_iter))


# object class
class MyClass5:
    pass


obj = MyClass5()
print("Object:", obj)

# oct()
print("Octal representation of 8:", oct(8))

# open()
with open("example.txt", "w") as f:
    f.write("Hello, World!")

# ord()
print("Ordinal value of 'A':", ord("A"))

# pow()
print("Power of 2 raised to 3:", pow(2, 3))

# print()
print("Hello, World!")


# property()
class MyClass6:
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value


obj = MyClass6()
obj.x = 42
print("Property value:", obj.x)

# range()
print("Range:", list(range(5)))

# repr()
print("Representation of 'Hello, World!':", repr("Hello, World!"))

# reversed()
print("Reversed list:", list(reversed([1, 2, 3])))

# round()
print("Rounded value of 3.14159:", round(3.14159, 2))

# set class
my_set = {1, 2, 3}
print("Set:", my_set)


# setattr()
class MyClass7:
    pass


obj = MyClass7()
setattr(obj, "attr", 42)
print("Attribute value:", obj.attr)

# slice class
sequence = [1, 2, 3, 4, 5]
my_slice = sequence[1:5:2]
print("Slice:", my_slice)

# sorted()
print("Sorted list:", sorted([3, 1, 2]))


# staticmethod()
class MyClass8:
    @staticmethod
    def my_method():
        print("Static method")


MyClass8.my_method()

# str class
print("String representation of 42:", str(42))

# sum()
print("Sum of [1, 2, 3]:", sum([1, 2, 3]))


# super()
class Parent:
    def __init__(self):
        self.name = "Parent"


class Child(Parent):
    def __init__(self):
        super().__init__()


child = Child()
print("Name of child:", child.name)

# tuple class
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)

# type()
print("Type of 'Hello, World!':", type("Hello, World!"))

# zip()
my_list1 = [1, 2, 3]
my_list2 = ["a", "b", "c"]
print("Zipped lists:", list(zip(my_list1, my_list2)))
