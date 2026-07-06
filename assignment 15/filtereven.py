even = lambda n: n%2 == 0

def main():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    result = list(filter(even, numbers))

    print("Original List:", numbers)
    print("Even List:", result)

if __name__ == "__main__":
    main()