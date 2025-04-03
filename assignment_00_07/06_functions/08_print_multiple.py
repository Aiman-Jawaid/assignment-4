def print_multiple(message, repeats):
    for _ in range(repeats):  # Repeat the message 'repeats' times
        print(message)

def main():
  
    BLUE = '\033[94m'
    RESET = '\033[0m'  


    message = input(f"{BLUE}Please type a message: {RESET}")  
    repeats = int(input(f"{BLUE}Enter a number of times to repeat your message: {RESET}"))  

    print_multiple(message, repeats)  

if __name__ == '__main__':
    main()
