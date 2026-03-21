# PYTHON WEIGHT CONVERTER
# CONVERTING KILOGRAM TO POUNDS AND OTHERWISE
weight = float(input("Enter your weight: "))
unit = input("kilograms or Pounds (kg or lbs): ")

if unit == "Kg":
    weight = weight * 2.205
    print(f"The Weight in Pounds(lbs) is: {round(weight, 2)}lbs")
elif unit == "lbs":   
    weight = weight / 2.205
    print(f"The Weight in Kilograms(Kg) is: {round(weight, 2)}Kg")
else:
    print(f"{unit} is not a valid unit")
