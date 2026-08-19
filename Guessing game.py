import random

print("🎮 Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")

# Computer random number pick chesthundi
secret_number = random.randint(1, 100)
guesses = 0

while True:
    guess = int(input("Enter your guess: "))
    guesses = guesses + 1

    if guess < secret_number:
        print("Too LOW! Try again ⬆️")
    elif guess > secret_number:
        print("Too HIGH! Try again ⬇️")
    else:
        print(f"🎉 CONGRATULATIONS! You guessed it in {guesses} tries!")
        break

print("Thanks for playing!")
