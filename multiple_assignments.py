"""Assigning multiple variables to the Same Value:
You can assign the same value to several variables simultaenously using the assignment operator chained together
"""
#e.g1
x= y= z= 10
print(x, y, z)

"""
Assigning Different Values to Multiple Variables:
You can assign different values to multiple variables and values with commas.
"""
# e.g1
name, age = "Laureate", 30
print(name)
print(age)

"""
This is a form of tuple unpacking. The number of variables on the left side of the 
= must match the number of values on the right side.
"""

"""
Swapping Variables:
Multiple assignment is commenly used to swap the values of two vatiables easily without needing a temporary varaible.
"""
#e.g1
a = 5
b = 10
a,b= b,a
print(a)
print(b)
