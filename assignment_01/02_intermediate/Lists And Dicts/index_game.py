def access_element(my_list, index):
    if 0 <= index < len(my_list):
        return f"Element at index {index}: {my_list[index]}"
    else:
        return "Index out of range."


def modify_element(my_list, index, new_value):
    if 0 <= index < len(my_list):
        old_value = my_list[index]
        my_list[index] = new_value
        return f"Replaced '{old_value}' with '{new_value}'."
    else:
        return "Index out of range."


def slice_list(my_list, start, end):
    if 0 <= start <= len(my_list) and 0 <= end <= len(my_list):
        return my_list[start:end]
    else:
        return "One or both indices are out of range."


def main():
   
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print("Welcome to the List Game!")
    print("Starting list:", my_list)

    while True:
        print("\nWhat would you like to do?")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Quit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            try:
                index = int(input("Enter index to access: "))
                print(access_element(my_list, index))
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '2':
            try:
                index = int(input("Enter index to modify: "))
                new_value = input("Enter new value: ")
                print(modify_element(my_list, index, new_value))
            except ValueError:
                print("Invalid input.")
        elif choice == '3':
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                result = slice_list(my_list, start, end)
                print("Sliced list:", result)
            except ValueError:
                print("Please enter valid numbers.")
        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please pick 1, 2, 3, or 4.")

        print("Current list:", my_list)


main()
