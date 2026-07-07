def checknum(no):
    if no>0:
        print("number is positive")
    elif no<0:
        print("number is negative")
    else:
        print("it is zero")


def main():
    num = int(input("enter a number:"))

    Ret = checknum(num)
    

if __name__ == "__main__":
    main()