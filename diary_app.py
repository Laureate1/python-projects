import datetime

print("Welcome to your Personal Diary App.")
name = input("What is your name? ")
print(f"Hello {name}, Your thoughts are safe here.")
print("You can write your thoughts and feelings here, and they will be stored securely.")

while True:
    print("\nWhat would you like to do?")
    print("1. Write a new entry")
    print("2. View all entries")
    print("3. Exit")
    
    choice = input("Enter your choice (1, 2 or 3): ")
    
    if choice == "1":
        entry = input("Write your entry: ")
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

        with open(f"{name}_diary.txt", "a") as file:
            file.write(f"\n {date}\n{entry}\n")
            file.write("-" * 40 + "\n")

        print("Entry saved successfully! 🥹")

    elif choice == "2":
        try:
            with open(f"{name}_diary.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No entries found yet! Write your first entry 🥹")

    elif choice == "3":
        print(f"Goodbye {name}! Your diary is safe 🥹")
        break

    else:
        print("Invalid choice! Please enter 1, 2 or 3.")