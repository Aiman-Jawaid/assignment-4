def in_range(n, low, high):
    return low <= n <= high

def main():
   
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    print(in_range(n, low, high))

if __name__ == '__main__':
    main()
