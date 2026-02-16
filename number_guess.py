import random

print("🎮 Welcome to the Number Guessing Game!")

# Computer picks a random number between 1 and 100
secret_number = random.randint(1, 100)

guess = 0

while guess != secret_number:
    guess = int(input("Enter your guess (1-100): "))

    if guess < secret_number:
        print("Too low! ⬇️")
    elif guess > secret_number:
        print("Too high! ⬆️")
    else:
        print("🎉 Correct! You guessed it!")

print("Game Over.")

