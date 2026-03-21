# The Circumference of a Circle
# The circumference of a circle is the distance around the circle. It can be calculated using the formula:
# Circumference = 2 * π * radius    

# To calculate the circumference of a circle, 
# we can write a Python program that takes the radius as input from the user and then uses the formula to calculate and print the circumference.    
import math 

# Take input from the user for the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate the circumference using the formula
circumference = 2 * math.pi * pow(radius, 1)     
# Print the circumference
print(f"The circumference of the circle is: {round(circumference, 2)}Cm")

