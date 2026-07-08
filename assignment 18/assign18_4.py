def Frequency(List, num):
    count = 0

    for i in List:
        if i == num:
            count = count + 1

    return count


def main():
    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    Data = list(map(int, input().split()))

    num = int(input("Enter element to search: "))

    Ret = Frequency(Data, num)

    print("Frequency of", num, "is:", Ret)


if __name__ == "__main__":
    main()