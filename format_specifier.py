# formatSPECIFIER = (value:flags)
# formats a value based on what flags are inserted in the format specifier. The format specifier is inserted after a colon (:) in an f-string.      

# e.g

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is {price1:.3f}")
print(f"price 2 is {price2:.3f}")
print(f"price 3 is {price3:.3f}")
# Output:
# price 1 is 3.142  
# price 2 is -987.650
# price 3 is 12.340
# In the above example, the format specifier is .3f, which means that the value should be formatted as a floating-point number with 3 decimal places. The output shows that the values have been rounded to 3 decimal places.
# Here are some common format specifiers and their meanings:
# f: formats a value as a floating-point number.
# d: formats a value as an integer.
# s: formats a value as a string.
# e: formats a value in scientific notation.
# %: formats a value as a percentage.
# Here are some more examples of using format specifiers:
number = 123.456789
print(f"number is {number:.2f}")
# Output:       
# number is 123.46
# In the above example, the format specifier .2f means that the number should be
#  formatted as a floating-point number with 2 decimal places. The output shows that the number has been rounded to 2 decimal places.    
# Here are some more examples of using format specifiers:
name = "Alice"
age = 30    
print(f"{name} is {age} years old.")
# Output:
# Alice is 30 years old.    
print(f"{name:10} is {age:5} years old.")
# Output:
# Alice      is    30 years old.
# In the above example, the format specifier :10 means that the name should be formatted
# with a minimum width of 10 characters, and the format specifier :5 means that the age should be formatted with a minimum width of 5 characters. The output shows that the name is left-aligned and the age is right-aligned within their respective widths.
print(f"{name:>10} is {age:<5} years old.")
# Output:
#      Alice is 30    years old.
# In the above example, the format specifier :>10 means that the name should be 
# right-aligned within a width of 10 characters, and the format specifier :<5 means that the age should be left-aligned within a width of 5 characters. The output shows that the name is right-aligned and the age is left-aligned within their respective widths. 
print(f"{name:^10} is {age:^5} years old.")
# Output:   
#   Alice    is  30   years old.
# In the above example, the format specifier :^10 means that the name should be centered within a width of 10 characters, and the format specifier :^5 means that the age should be centered within a width of 5 characters. 
# The output shows that both the name and age are centered within their respective widths.
# e.g   
number = 123456789
print(f"{number:,}")    
# Output:
# 123,456,789
# In the above example, the format specifier :, means that the number should be formatted with
# a comma as a thousands separator. The output shows that the number is formatted with commas to separate the thousands.

