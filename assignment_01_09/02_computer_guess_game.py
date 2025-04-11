import random

def computer_guesses_number():
    print("Think of a number between 1 and 100 and I will try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    feedback = ''
    guesses = 0

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Only one number left

        guesses += 1
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Please enter H, L, or C.")

    print(f"🎉 Yay! I guessed your number {guess} in {guesses} tries!")

# Run the game
computer_guesses_number()
