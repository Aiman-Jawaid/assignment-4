def main():
    
    first_number = int(input("\033[1;3m Please enter an integer to be divided: \033[0m"))
    second_number = int(input("\033[1;3m Please enter an integer to divide by: \033[0m"))
    
    
    quotient = first_number // second_number
    remainder = first_number % second_number
    
    print(f"The result of this division is {quotient} with a remainder of {remainder}")


if __name__ == '__main__':
    main()
