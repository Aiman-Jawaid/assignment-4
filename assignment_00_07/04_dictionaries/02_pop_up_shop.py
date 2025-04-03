def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    
    for fruit_name, price in fruits.items():
        while True:
            amount_bought = input(f"\033[1;3m How many ({fruit_name}) do you want to buy? (Enter 0 to skip): \033[0m")
            
            if amount_bought.lower() == "exit":
                print("Exiting early...")
                print(f"Your total is ${total_cost:.2f}")
                return  # Exit program immediately

            if amount_bought.isdigit():  # Ensure input is a valid number
                amount_bought = int(amount_bought)
                total_cost += price * amount_bought
                break
            else:
                print("Invalid input! Please enter a number.")

    print(f"Your total is ${total_cost:.2f}")

if __name__ == '__main__':
    main()
