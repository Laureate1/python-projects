
item = input("Enter an item: ")
price = float(input("Enter the price: "))
quantity = int(input("how many items would you like to purchase: "))

Total = price * quantity

print(f"you have bought {quantity} {item}/s")
print(f"your total is : ${round(Total, 2)}")