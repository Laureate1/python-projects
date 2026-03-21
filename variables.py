# A variable is a container for a value of a specific data type( String, integer, Float, Boolean )
# A variable behaves as if it was the value it contains
# To assign a variable, you use the assignment operator ("=")

#TYPES OF VAARIABLES

#STRINGS( A string is a series of characters(they can include numbers but we treat them as characters) always in quotes).
#e.g1
first_name = "Laureate"
print(first_name)

#this will output first_name which is "Laureate"
#if you print in quote i.e("first_name")it will take first_name as a string instead of Laureate.

#CONCATENATION(Using the + operator to join strings)
#e.g1
greeting = "Hello" + " " + "Python"
print(greeting)

#REPITITION( Using the * operator)
#e.g1
repeat = "abc" * 3
print(repeat)

"""INDEXING( Accessing individual characters using square brackets "[]".
Indexing starts from 0. Negative indices counts from the end)"""
#e.g1
my_string = "Python"
print(my_string[0])
print(my_string[-1])

#SLICING(Extracting a portion of string using [start, stop, step]. The "stop" index is exclusive)
#e.g1
print(my_string[0:3])
print(my_string[::2])

#STRING METHODS(Functions like .upper(), .lower(), .strip(), .split(), .replace(), .find(), etc)
#e.g1
name = " Alice "
print(name.strip())
print("hello".upper())

#you could use your variable along with some texts by using what is called an f-string 
#e.g 1
food ="pizza"
email="laureate@fake.com"
print(f"Hello {first_name}") #give you the output "Hello Laureate"
print(f"Your email is {email}") # give you the output "Your email is laureate@fake.com"

#INTEGERS( An integer is both positive and negative whole numbers).
#e.g 1 
age = 25
quantity = 3
num_of_students = 50
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#FLOAT(A float is a datatype that represents a decimal numbers)
#e.g1
price = 10.99
gpa = 3.58 
distance = 5.5
print(f"The price is ${price}")
print(f"Your gpa is {gpa}")
print(f"You ran a distance of {distance}km")

#BOOLEAN( A boolean is either a true or false statement)
#e.g1
is_student =True
print(f"Are you a student?: {is_student}")

#BOOLEAN OPERATIONS
"""
and: Returns True if both operands are true
or: Returns true if at least one operand is true 
not: Negates the boolean value(not True is False, not False is True)"""
#e.g1
is_sunny = True
is_warm = False
print(is_sunny and is_warm)
print(is_sunny or is_warm)
print(not is_warm)

# COMPARISON OPERATORS (Boolean values are usually the result of comparison operations)
"""
Equal to: ==
Not equal to: !=
Greater than: >
Less than: <
Greater than or equal to: >=
Less than or equal to: <=
"""
#e.g
print(10 > 5)
print(5 == 5)
print("hello" != "world")
