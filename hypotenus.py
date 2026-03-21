#the hypotenus of a right triangle can be calculated using the formula:
# hypotenus = sqrt(a^2 + b^2)
# where a and b are the lengths of the two legs of the triangle.    

import math

a = float(input("Enter the length of side (a): "))
b = float(input("Enter the length of side (b): "))

hypotenus = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenus of the right triangle is: {round(hypotenus, 2)}")