def checkNum(no):
    if no %2 == 0:
        print("Even number")
    else:
        print("Odd number")

def main():
    num = int(input("enter the number:"))

    Ret = checkNum(num)

    

if __name__ == "__main__":
    main()