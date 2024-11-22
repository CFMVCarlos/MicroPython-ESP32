from collections import OrderedDict, namedtuple

# Using namedtuple
print("\nUsing namedtuple:")
# Creating a namedtuple type with fields 'id' and 'name'
MyTuple = namedtuple("MyTuple", ("id", "name"))
# Creating instances of MyTuple
t1 = MyTuple(1, "foo")
t2 = MyTuple(2, "bar")
# Accessing fields using attribute access syntax
print("Name of t1:", t1.name)
print("Name of t2:", t2.name)
assert t2.name == t2[1]


# Using OrderedDict
print("\nUsing OrderedDict:")
# Creating an OrderedDict with initial key-value pairs
d = OrderedDict([("z", 1), ("a", 2)])
# Adding more items to the OrderedDict
d["w"] = 5
d["b"] = 3
# Iterating over the OrderedDict
print("Iterating over the OrderedDict:")
for k, v in d.items():
    print(k, v)
