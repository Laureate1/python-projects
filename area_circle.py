# AREA OF A CIRCLE
# The area of a circle is calculated using the formula:
# Area = π * radius^2   
# To calculate the area of a circle, we can write a Python program that takes the radius as input from the user and then
# uses the formula to calculate and print the area.
# Take input from the user for the radius
import math   

radius = float(input("Enter the radius of the circle: "))   

# Calculate the area using the formula
area = math.pi * pow(radius, 2)
# Print the area
print(f"The area of the circle is: {round(area, 2)}Cm^2") 

