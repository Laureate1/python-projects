#USER INPUT IN PYTHON
#To take input from the user, we can use the input() function in Python. 
# This function reads a line of text from the user and returns it as a string. 
# Here are some examples of how to use the input() function:
#E.G1
name = input("What is your name? ")
age = input("How old are you? ")
favorite_color = input("What is your favorite color? ")

print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"Your favorite color is {favorite_color}.")

#Note that the input() function always returns a string, so if you want to convert the input to a different datatype (like an integer or float), you can use type conversion functions like int() or float().