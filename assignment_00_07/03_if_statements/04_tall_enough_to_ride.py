MINIMUM_HEIGHT: int = 50  

def main():
    while True:
        try:
           
            height_input = input("\033[1;3m How tall are you? (Press Enter to quit) \033[0m")
            
            
            if height_input == "":
                print("Goodbye!")
                break
            
            
            height = float(height_input)
            
           
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        
        except ValueError:
            print("Please enter a valid number for your height.")


if __name__ == '__main__':
    main()
