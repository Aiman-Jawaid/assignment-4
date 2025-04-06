import random

NUM_ROUNDS = 5
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        # Generate random numbers
        your_number = random.randint(MIN_VALUE, MAX_VALUE)
        computer_number = random.randint(MIN_VALUE, MAX_VALUE)
        
        print(f"Your number is {your_number}")
        
        # Get user input
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        
        # Input safeguard
        while guess not in ["higher", "lower"]:
            guess = input("Please enter either higher or lower: ").lower()

        # Game logic
        if your_number == computer_number:
            correct = False  # Same number is always a loss
        elif guess == "higher":
            correct = your_number > computer_number
        elif guess == "lower":
            correct = your_number < computer_number
        
        # Result and score tracking
        if correct:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}\n")

    # End of game message
    print("Thanks for playing!")
    print(f"Your final score is {score}")

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()
