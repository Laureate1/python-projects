# Password Checker
# This program checks the strength of a password based on certain criteria.
# The criteria for a strong password are:       
# 1. At least 8 characters long
# 2. Contains both uppercase and lowercase letters
# 3. Contains at least one digit
# 4. Contains at least one special character (e.g., !, @, #, $, etc.)

print("Welcome to the Password Strength Checker")
password = input("Enter your password: ")
print(f"\nChecking password: {password}")

score = 0

if len(password) >= 8:
    score += 2

if any(char.isupper() for char in password):
    score += 2

if any(char.islower() for char in password):
    score += 2

if any(char.isdigit() for char in password):
    score += 2

if any(char in "!@#$%^&*()_+-=[]{}|;':,./<>?" for char in password):
    score += 2

print(f"Your score is: {score}/10")

if score <= 4:
    print("Password Strength: WEAK")
    print("Tips to improve:")
    print("- Add uppercase letters")
    print("- Add numbers")
    print("- Add special characters like !@#$%")
elif score <= 8:
    print("Password Strength: MODERATE")
    print("Getting better! Try adding more variety to make it stronger.")
else:
    print("Password Strength: STRONG")
    print("Great job! Your password is very secure.")   
print("\nThank you for using the Password Strength Checker, Stay safe online!")