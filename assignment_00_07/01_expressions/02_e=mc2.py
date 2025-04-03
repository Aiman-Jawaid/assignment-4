def main():
    
    C = 299792458  
    
    while True:
        try:
            mass_input = input("Enter kilos of mass (or type 'exit' to quit): ")
            
            
            if mass_input.lower() == "exit":
                print("Exiting program...")
                break  
            
            mass = float(mass_input)  
            energy = mass * C**2  
            
           
            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s")
            print(f"{energy} joules of energy!\n")
        
        except ValueError:
            print("Please enter a valid number for mass or type 'exit' to quit.\n")

if __name__ == '__main__':
    main()


