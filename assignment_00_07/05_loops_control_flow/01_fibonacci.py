def main():
    MAX_VALUE = 10000
    fib1, fib2 = 0, 1
    
    print(fib1, end=" ")
    while fib2 < MAX_VALUE:
        print(fib2, end=" ")
        fib1, fib2 = fib2, fib1 + fib2
    
    print()  # For a new line at the end

if __name__ == '__main__':
    main()
