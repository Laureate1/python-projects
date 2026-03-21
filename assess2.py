# # # SECTION C

# # 11.Ask the user for their full name and make sure:
# # extra spaces are removed
# # each word starts with capital letter

# name = input("Enter your full name: ")
# space = name.strip()
# word = name.title()
# print(space)
# print(word)

# # 12. Write a program that checks if the user typed only letters.
# username =input("Enter your name: ")
# if username.isalpha():
#     print(f"Welcome {username}")
# else:
#     print("Invalid username!!")

# # 13.
# user_age =input("Enter your age: ")
# if user_age.isdigit():
#     print(f"{user_age} Accepted")

# else:
#     print("Invalid Age!!")

# # 14. Write a program that checks if the user typed only letters and numbers.
# user = input("Enter your username: ")
# if user.isalnum():
#      print(f"Welcome {user}")  
# else:
#     print("Invalid username!!")

# # 15.Write a small program that asks the user for an email and checks:
# # if it contains "@"
# # and contains "."

# email = input("Enter your email: ")
# if "@" in email and "." in email:
#     print("Valid email address.")
# else:
#     print("Invalid email address.")

# 16. the answer is because the name.upper was not assigned to a variable, 
# so it did not change the original name variable. To fix it, 
# we can assign the result of name.upper() back to the name variable like this: name = name.upper().

# 17. because of the importance of passwords, write a program that checks if the password is strong enough. A strong password should contain at least 8 characters, at least one uppercase letter, at least one lowercase letter, and at least one digit.
password = input("Enter your password: ")   
if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() 
for char in password) and any(char.isdigit() for char in password):
    print("Strong password.")
else:    
    print("Weak password. Please ensure it has at least 8 characters, including uppercase letters, lowercase letters, and digits.")

# # 18. Write a program that checks if the user typed a valid phone number. A valid phone number should contain only digits and be 10 characters long.
# phone_number = input("Enter your phone number: ")   
# if phone_number.isdigit() and len(phone_number) == 10:
#     print("Valid phone number.")    
# else:    print("Invalid phone number. Please enter a 10-digit number containing only digits.")

# # 19. Write a program that checks if the user typed a valid URL. A valid URL should start with "http://" or "https://".
# url = input("Enter a URL: ")        
# if url.startswith("http://") or url.startswith("https://"):
#     print("Valid URL.") 
# else:    print("Invalid URL. Please ensure it starts with 'http://' or 'https://'.")        
