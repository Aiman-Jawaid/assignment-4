import random

def roll_dice():
    return random.randint(1, 6)

def main():
    for i in range(3):  
        die1 = roll_dice()
        die2 = roll_dice()
        print(f"Roll {i + 1}: Die 1 = {die1}, Die 2 = {die2}")


if __name__ == '__main__':
    main()
