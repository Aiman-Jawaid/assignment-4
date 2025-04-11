import random

def guess_the_number():
    top_of_range = input("Enter the maximum number: ")

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range <= 0:
            print("Please enter a number greater than 0 next time.")
            return
    else:
        print("Please enter a valid number.")
        return

    secret_number = random.randint(1, top_of_range)
    guess = 0
    attempts = 0

    while guess != secret_number:
        guess = input(f"Guess a number between 1 and {top_of_range}: ")

        if guess.isdigit():
            guess = int(guess)
        else:
            print("Please enter a number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    print(f"🎉 Congrats! You guessed the number {secret_number} in {attempts} tries!")

# Run the game
guess_the_number()
