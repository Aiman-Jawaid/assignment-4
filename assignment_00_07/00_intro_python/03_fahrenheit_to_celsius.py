def main():

    fahrenheit = float(input(" \033[1;3m Enter temperature in Fahrenheit: \033[0m "))

    celsius = (fahrenheit - 32.00) * (5.00/9.00)

    print(f"Temperature in Fahrenheit: {fahrenheit:.2f} \nTemperature in Celsius: {celsius:.2f}")

if __name__ == "__main__":
    main()
