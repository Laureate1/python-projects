# LOGICAL OPERATORS IN PYTHON
# AND = both conditions must be True    
# OR = Checks if at least one is True
# not = True if condition is False and vice versa

# e.g1
temp = 45
if temp > 0 and temp < 30:
    print("The temperature is good")
else:
    print("The temperature is bad")
if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")

is_sunny = True

if not (is_sunny):
    print("It is raining")
else: 
    print("The weather is sunny")
