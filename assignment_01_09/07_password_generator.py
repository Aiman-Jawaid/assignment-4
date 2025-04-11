import random
import string

def generate_password(length):
   
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")


    try:
        num_passwords = int(input("How many passwords would you like to generate? "))
        password_length = int(input("What should be the length of each password? "))
        
        if num_passwords <= 0 or password_length <= 0:
            print("Please enter positive numbers for both fields.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

   
    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        print(generate_password(password_length))


main()
