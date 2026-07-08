import MarvellousNum

def listprime(List):
    Sum = 0

    for i in List:
        if MarvellousNum.chkprime(i):
            Sum = Sum + i

    return Sum


def main():
    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    Data = list(map(int, input().split()))

    Ret = listprime(Data)

    print("Addition of prime numbers is:", Ret)


if __name__ == "__main__":
    main()