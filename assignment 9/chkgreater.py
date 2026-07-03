def chkgreater(No1,No2):
    if(No1>No2):
        print("first number is greater",No1)
    else:
        print("second number is greater",No2)


def main():
    value1 = int(input("enter first number"))
    Value2 = int(input("enter second number"))

    chkgreater(value1,Value2)

if __name__ == "__main__":
    main()
