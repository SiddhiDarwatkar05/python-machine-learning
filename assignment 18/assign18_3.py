def Minimum(List):
    Min = List[0]

    for i in List:
        if i < Min:
            Min = i

    return Min


def main():
    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    Data = list(map(int, input().split()))

    Ret = Minimum(Data)

    print("Minimum number is:", Ret)


if __name__ == "__main__":
    main()