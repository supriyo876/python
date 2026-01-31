import random

print("Welcome to Number Guessing Game!")
print("Guess a number, dear 😉")

secret = random.randint(1, 100)
guess = None
attempt = 0

while guess != secret:
    try:
        guess = int(input("Guess a number: "))
        attempt += 1

        if guess < secret:
            print("Areee mogaaa! You entered a lower number 😅")
        elif guess > secret:
            print("Moga! You entered a higher number 😆")
        else:
            print(f"Correct number haha! The secret number was {secret}.")
            print(f"You got it in {attempt} attempts! 🎯")

    except ValueError:
        print("Keep your eyes open moga 😜 — enter a valid number!")
