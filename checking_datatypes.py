# Python provides a built-in function called `type()` that can be used to check the datatype of a variable.
# Here are some examples of how to use it:

my_variable = "hello"
print(type(my_variable)) # Output: <class 'str'>

another_variable = 123
print(type(another_variable)) # Output: <class 'int'>

pi_value = 3.14
print(type(pi_value)) # Output: <class 'float'>

is_active = True
print(type(is_active)) # Output: <class 'bool'>

# You can also check the datatype of a constant defined in constants.py
from constants import PI, Max_CONNECTIONS, SITE_NAME
print(type(PI)) # Output: <class 'float'>
print(type(Max_CONNECTIONS)) # Output: <class 'int'>
print(type(SITE_NAME)) # Output: <class 'str'>

# Additionally, you can check the datatype of variables that have been assigned multiple values in multiple_assignments.py
from multiple_assignments import x, y, z, name, age, a, b
print(type(x)) # Output: <class 'int'>
print(type(name)) # Output: <class 'str'>
print(type(age)) # Output: <class 'int'>
print(type(a)) # Output: <class 'float'>
print(type(b)) # Output: <class 'bool'>

# THE ISINSTANCE() FUNCTION
# the isinstance() function can also be used to check if a variable is of a specific datatype
print(isinstance(my_variable, str)) # Output: True
print(isinstance(another_variable, int)) # Output: True


# You can also check for multiple datatypes using isinstance() with a tuple of types
print(isinstance(pi_value, (int, float))) # Output: True
print(isinstance(is_active, (str, bool))) # Output: True

# isinstance() is generally preferred over type() for checking datatypes, 
# especially when dealing with inheritance, as it considers subclass relationships.

