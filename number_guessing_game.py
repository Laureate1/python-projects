# import random

# secret_number = random.randint(1, 100)
# print("Welcome to the Number Guessing Game!")
# print("I have picked a number between 1 and 100.")
# print("Can you guess what it is?")

# attempts = 0
# while True:
#     guess = int(input("Enter your guess: "))
#     attempts += 1

#     if guess < secret_number:
#         print("Too low! Try again.")
#     elif guess > secret_number:
#         print("Too high! Try again.")
#     else:
#         print(f"Congratulations! You've guessed the number {secret_number} correctly! and You guessed it in {attempts} attempts")
#         break

import random

def play_game():
    secret_number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game! 🎮")
    print("I have picked a number between 1 and 100.")
    print("You have 10 attempts. Good luck! 🍀/n")

    attempts = 0

    while attempts < 10:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print(f"Too low! {10 - attempts} attempts remaining.")
        elif guess > secret_number:
            print(f"Too high! {10 - attempts} attempts remaining.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts!")
            break
    else:
        print(f"😭 Game over! The number was {secret_number}.")

    play_again = input("\nPlay again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thanks for playing!🙌🏽 ")

play_game()
