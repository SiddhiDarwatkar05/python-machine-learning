def AdditionFactors(no):
    sum = 0

    for i in range(1, no):
        if no % i == 0:
            sum = sum + i

    return sum


def main():
    num = int(input("Enter a number: "))

    Ret = AdditionFactors(num)

    print("Addition of factors is:", Ret)


if __name__ == "__main__":
    main()