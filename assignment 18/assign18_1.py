def Addition(lst):
    sum = 0

    for i in lst:
        sum = sum + i

    return sum


def main():
    size = int(input("Enter number of elements: "))

    data = list(map(int, input("Enter elements: ").split()))

    Ret = Addition(data)

    print("Addition of all elements is:", Ret)


if __name__ == "__main__":
    main()