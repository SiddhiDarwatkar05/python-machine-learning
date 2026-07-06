Square = lambda x: x * x

def main():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    result = list(map(Square, numbers))

    print("Original List:", numbers)
    print("Square List:", result)

if __name__ == "__main__":
    main()