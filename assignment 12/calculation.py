def calc(no1,no2):
    addition= no1+no2
    subtraction=no1-no2
    multiplication=no1*no2
    division=no1/no2
    return addition,subtraction,multiplication,division


def main():
    value1=int(input("enter the first number:"))
    value2=int(input("enter the second number:"))

    add,sub,mul,div = calc(value1,value2)

    print("addition is:",add)
    print("subtraction is:",sub)
    print("multiplication is:",mul)
    print("division is:",div)

if __name__ == "__main__":
    main()