def Maximum(List):
    Max = List[0]

    for i in List:
        if i > Max:
            Max = i

    return Max


def main():
    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    Data = list(map(int, input().split()))

    Ret = Maximum(Data)

    print("Maximum number is:", Ret)


if __name__ == "__main__":
    main()