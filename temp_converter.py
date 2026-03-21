
# temperature conversion
unit = input("Enter the unit of temperature (C for Celsius, F for Fahrenheit): ")
temp = float(input("Enter the temperature: "))  
if unit == "C":
    total_temp = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {round(total_temp, 2)}°F")
elif unit == "F":
    total_temp = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {round(total_temp, 2)}°C")
else:
    print(f"{unit} is not a valid unit")

# how can i convert this code to a website or app for use