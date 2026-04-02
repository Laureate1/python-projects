import random

print("Welcome to the Username Generator.")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

first = first_name.lower()
last = last_name.lower()
rand_num = random.randint(100, 999)

usernames = [
    f"{first}_{last}",
    f"{first}{rand_num}",
    f"{first}.{last}",
    f"{last}_{first}{rand_num}",
    f"{first[0]}{last}{rand_num}",
]

print("\nHere are your generated usernames to choose from:")

for i, username in enumerate(usernames, 1):
    print(f"{i}. {username}")

choice = int(input("\nPick your favourite (1-5): "))
print(f"\nGreat choice, your username is: @{usernames[choice - 1]}")
play_again = input("\nGenerate new usernames? (yes/no): ")
if play_again.lower() == "yes":
    rand_num = random.randint(100, 999)
    usernames = [
        f"{first}_{last}",
        f"{first}{rand_num}",
        f"{first}.{last}",
        f"{last}_{first}{rand_num}",
        f"{first[0]}{last}{rand_num}",
    ]
    print("\nHere are your new usernames:")
    for i, username in enumerate(usernames, 1):
        print(f"{i}. {username}")
    choice = int(input("\nPick your favourite (1-5): "))
    print(f"\nGreat choice, your username is: @{usernames[choice - 1]}")
else:
    print("\nThank you for using the Username Generator, enjoy your new username")
  
