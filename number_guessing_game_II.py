import random

high_score = 0

def get_difficulty():
    print("Choose your difficulty level:")
    print("1. Easy (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard (1 - 200)")
    
    choice = input("Enter 1, 2 or 3: ")
    
    if choice == "1":
        return 50, "Easy"
    elif choice == "2":
        return 100, "Medium"
    elif choice == "3":
        return 200, "Hard"
    else:
        print("Invalid choice! Defaulting to Medium 😄")
        return 100, "Medium"

def play_game():
    global high_score
    
    print("\n🎮 Welcome to the Number Guessing Game.")
    print("----------------------------------------")
    
    # Get difficulty
    limit, difficulty = get_difficulty()
    secret_number = random.randint(1, limit)
    
    print(f"\n✅ {difficulty} mode selected!")
    print(f"I have picked a number between 1 and {limit}.")
    print("You have 10 attempts. Good luck!\n")
    
    attempts = 0
    
    while attempts < 10:
        guess = int(input("Enter your guess: "))
        attempts += 1
        remaining = 10 - attempts
        
        # Hint system every 3 wrong guesses
        if attempts % 3 == 0 and guess != secret_number:
            if secret_number % 2 == 0:
                print("💡 Hint: The number is EVEN!")
            else:
                print("💡 Hint: The number is ODD!")
        
        if guess < secret_number:
            print(f"Too low! {remaining} attempts remaining.")
        elif guess > secret_number:
            print(f"Too high! {remaining} attempts remaining.")
        else:
            print(f"\n🎉 CORRECT!! You guessed it in {attempts} attempts!")
            
            # High score tracker
            if high_score == 0 or attempts < high_score:
                high_score = attempts
                print(f"🏆 New High Score: {high_score} attempts!")
            else:
                print(f"🏆 Your Best Score: {high_score} attempts!")
            break
    else:
        print(f"\n😭 Game over! The number was {secret_number}.")

    play_again = input("\nPlay again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print(f"\n👋 Thanks for playing!")
        print(f"🏆 Your Best Score: {high_score} attempts!")
play_game()