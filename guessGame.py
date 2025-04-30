import random

secret_number = random.randint(1, 20)  # You can adjust the range
attempts = 5

print("Guess the number between 1 and 20. You have 5 attempts!")

for i in range(attempts):
    user_input = input(f"\nAttempt {i + 1}: Enter your guess: ")

    if not user_input.isdigit():
        print("Invalid input! Please enter a number.")
        continue  # Skip this attempt, doesn't count

    guess = int(user_input)

    if guess == secret_number:
        print(" Correct! You guessed the number.")
        break
    elif guess < secret_number:
        print("You Guessed low!")
    else:
        print("You Guessed high!")

else:
    print(f"\n Sorry! You've used all attempts. The number was {secret_number}.")

