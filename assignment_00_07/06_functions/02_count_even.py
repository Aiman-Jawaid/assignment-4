def count_even(lst):
    # Counting the number of even numbers in the list
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
    print(f"Number of even numbers: {even_count}")

def main():
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            num = int(user_input)
            lst.append(num)
        except ValueError:
            print("Please enter a valid integer.")
    
    count_even(lst)

if __name__ == '__main__':
    main()
