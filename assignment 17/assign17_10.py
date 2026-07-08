def AddDigits(no):
    sum = 0

    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10

    return sum


def main():
    num = int(input("Enter a number: "))

    Ret = AddDigits(num)

    print("Addition of digits is:", Ret)


if __name__ == "__main__":
    main()