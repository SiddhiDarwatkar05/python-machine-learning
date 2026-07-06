from functools import reduce

min = lambda no1,no2:(no1 if no1< no2 else no2)

def main():
    num = list(map(int,input("enter sequence of numbers with space: ").split()))

    Ret = reduce(min,num)

    print("minimum no is:",Ret)

if __name__ == "__main__":
    main()