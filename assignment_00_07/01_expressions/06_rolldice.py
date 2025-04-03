import random

def main():
   
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    
    
    print(f"You rolled a {die1} and a {die2}.")
    print(f"Total: {total}")


if __name__ == '__main__':
    main()
