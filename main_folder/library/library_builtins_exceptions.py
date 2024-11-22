# AssertionError
try:
    assert False, "Assertion failed"
except AssertionError as e:
    print("Caught AssertionError:", e)


# AttributeError
class MyClass:
    pass


try:
    obj = MyClass()
    print(obj.nonexistent_attribute)
except AttributeError as e:
    print("Caught AttributeError:", e)

# Exception
try:
    raise Exception("Custom exception")
except Exception as e:
    print("Caught Exception:", e)

# ImportError
try:
    import non_existent_module
except ImportError as e:
    print("Caught ImportError:", e)

# IndexError
my_list = [1, 2, 3]
try:
    print(my_list[4])
except IndexError as e:
    print("Caught IndexError:", e)

# KeyboardInterrupt
try:
    print("Press Ctrl+C to raise KeyboardInterrupt...")
    while True:
        pass
except KeyboardInterrupt:
    print("Caught KeyboardInterrupt")

# KeyError
my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])
except KeyError as e:
    print("Caught KeyError:", e)

# MemoryError
try:
    my_list = [0] * 10**9
except MemoryError:
    print("Caught MemoryError")

# NameError
try:
    print(undefined_variable)
except NameError as e:
    print("Caught NameError:", e)

# NotImplementedError
try:
    raise NotImplementedError("Not implemented yet")
except NotImplementedError as e:
    print("Caught NotImplementedError:", e)

# OSError
try:
    f = open("non_existent_file.txt", "r")
except OSError as e:
    print("Caught OSError:", e)

# RuntimeError
try:
    raise RuntimeError("Runtime error occurred")
except RuntimeError as e:
    print("Caught RuntimeError:", e)

# StopIteration
iterator = iter([1, 2, 3])
try:
    while True:
        print(next(iterator))
except StopIteration as e:
    print("Caught StopIteration:", e)

# SyntaxError
try:
    exec('print"Syntax error")')
except SyntaxError as e:
    print("Caught SyntaxError:", e)

# SystemExit
try:
    raise SystemExit("Exiting")
except SystemExit as e:
    print("Caught SystemExit:", e)

# TypeError
try:
    42 + "abc"
except TypeError as e:
    print("Caught TypeError:", e)

# ValueError
try:
    int("abc")
except ValueError as e:
    print("Caught ValueError:", e)

# ZeroDivisionError
try:
    result = 1 / 0
except ZeroDivisionError as e:
    print("Caught ZeroDivisionError:", e)
