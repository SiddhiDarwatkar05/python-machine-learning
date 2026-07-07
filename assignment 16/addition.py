def add(no1,no2):
    Ans = no1+no2
    return Ans

def main():
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))

    Ret = add(num1,num2)
    print("Addition is:",Ret)

if __name__ == "__main__":
    main()