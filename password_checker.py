# Password Checker
# This program checks the strength of a password based on certain criteria.
# The criteria for a strong password are:       
# 1. At least 8 characters long
# 2. Contains both uppercase and lowercase letters
# 3. Contains at least one digit
# 4. Contains at least one special character (e.g., !, @, #, $, etc.)
import re   

def check_password_strength(password):
    # Check if password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if password contains both uppercase and lowercase letters
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return False

    # Check if password contains at least one digit
    if not re.search(r'\d', password):
        return False

    # Check if password contains at least one special character
    if not re.search(r'[!@#$%^&*()-+]', password):
        return False

    return True