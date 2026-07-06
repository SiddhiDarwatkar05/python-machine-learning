odd = lambda n: n%2 !=0

def main():
    numbers = list(map(int,input("enter numbers separated by space:").split()))

    result = list(filter(odd,numbers))

    print("original list is:",numbers)
    print("odd sequence list is:",result)

if __name__ == "__main__":
    main()