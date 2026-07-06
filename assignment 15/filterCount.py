count = lambda n: n%2 == 0

def main():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    result = list(filter(count, numbers))

    
    print(" count of even number is:",len(result))

if __name__ == "__main__":
    main()