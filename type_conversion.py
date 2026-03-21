# Type convesion can also be called type Casting(The process of turning a value of one data type to another)
# Python provides built-in functions for converting between common types

# int(x): Convert a number or string to an integer, or return 0 if no arguments are given. 
# e.g1
print(int(3.14))
print(int("100"))

# print(int("hello")): this would cause a ValueError

# float(x): Converts x to a floating point number. Can convert integers or strings(if they represent a valid float or integer)
# e.g1
print(float(5))
print(float("2.718")) 

# str(x): Converts x to a string representation. Can convert numbers, booleans, and oter objects.
# e.g1
print(str(123))
print(str(True))

"""bool(x): Converts x to a Boolean value. Most values are considered True. Values considered False include 0, 0.0, empty tuples(),
empty dictionaries{}, and None."""
# e.g1
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("hello"))