def get_user_numbers():
    """
    Get a list of numbers from the user until they enter a blank line.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("Please enter a valid number.")
    return user_numbers

def count_nums(num_lst):
    """
    Count occurrences of each number in the list using a dictionary.
    """
    num_dict = {}
    for num in num_lst:
        num_dict[num] = num_dict.get(num, 0) + 1
    return num_dict

def print_counts(num_dict):
    """
    Print out each number and the number of times it appears.
    """
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")

def main():
    """
    Collect user numbers, count occurrences, and print results.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()
