import random

print("🎯 Welcome to the Number Guessing Game!")

# Difficulty selection
print("\nSelect difficulty:")
print("1 - Easy (1 to 10)")
print("2 - Medium (1 to 50)")
print("3 - Hard (1 to 100)")

choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    max_number = 10
elif choice == "2":
    max_number = 50
elif choice == "3":
    max_number = 100
else:
    print("Invalid choice. Defaulting to Easy.")
    max_number = 10

secret_number = random.randint(1, max_number)
attempts = 0
score = 100

print(f"\nI'm thinking of a number between 1 and {max_number}...")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
        score -= 10

        if guess < secret_number:
            print("Too low! 📉")
        elif guess > secret_number:
            print("Too high! 📈")
        else:
            print("\n🎉 Correct!")
            print(f"You guessed it in {attempts} attempts.")
            print(f"Your final score is: {score}")
            break
    except ValueError:
        print("Please enter a valid number.")
