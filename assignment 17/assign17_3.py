def factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact * i
    return fact

def main():
    num = int(input("enter a number:"))
    ret = factorial(num)
    print("factor is:",ret)

if __name__ == "__main__":
    main()

