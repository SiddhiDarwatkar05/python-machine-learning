def CountDigits(no):
    count = 0

    while no > 0:
        no = no // 10
        count = count + 1

    return count


def main():
    num = int(input("Enter a number: "))

    Ret = CountDigits(num)

    print("Number of digits are:", Ret)


if __name__ == "__main__":
    main()