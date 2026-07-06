from functools import reduce

add = lambda no1,no2:(no1+no2)

def main():
    num = list(map(int,input("enter sequence of numbers with space: ").split()))

    Ret = reduce(add,num)

    print("addition is:",Ret)

if __name__ == "__main__":
    main()