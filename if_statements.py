# IF STATEMENT
# An if statement is a conditional statement that allows you to execute a block of code only if a certain condition is true. The basic syntax of an if statement in Python is as follows:
"""         
if condition:
    # code to execute if the condition is true
    if = Do some code only IF some condition is true
         ELSE do something else
"""

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.") 
elif age < 0:
    print("You are yet to be born.")
elif age > 100:
    print("You are a too old to sign up.")
else:
    print("You are a minor and must be 18+ to be an adult.")

# E.g2
# response = input("Do you like Python? (yes/no): ")
# if response == "":  
#     print("Please enter a valid response.")
# if response == "yes":
#     print("Great! Python is a wonderful programming language.") 
# elif response == "no":
#     print("That's okay! Python isn't for everyone.")
