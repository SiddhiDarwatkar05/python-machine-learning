from functools import reduce

product = lambda no1,no2:(no1*no2)

def main():
    num = list(map(int,input("enter numbers with space:").split()))

    Ret = reduce(product,num)

    print("product of list is:",Ret)

if __name__ == "__main__":
    main()