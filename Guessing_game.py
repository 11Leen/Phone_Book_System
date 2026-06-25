print("NEW VERSION")
import random

while True:
    print("\n--- Guessing Game ---")
    print("1. Easy (number between 1 and 10)")
    print("2. Middle (number between 1 and 20)")
    print("3. Hard (number between 1 and 50)")
    print("4. Finish")

    choice = input("Enter num: ")

    if choice == "1":
        secret_number = random.randint(1, 10)
        attempts = 7
        level = "Easy"
    elif choice == "2":
        secret_number = random.randint(1, 20)
        attempts = 5
        level = "Middle"
    elif choice == "3":
        secret_number = random.randint(1, 50)
        attempts = 3
        level = "Hard"
    elif choice == "4":
        print("Finish")
        break
    else:
        print("Invalid choice.")
        continue

    print(f"\nYou chose {level} level. You have {attempts} attempts!")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess == secret_number:
            print("🎉 Correct! You guessed the number!")
            break
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

        attempts -= 1
        print("Attempts left:", attempts)

        if attempts == 0:
            print("😢 Out of attempts! The number was:", secret_number)

    play_again = input("Do you want to play again? (Yes/No): ")
    if play_again.lower() != "yes":
        print("Good bye! 👋")
        break


