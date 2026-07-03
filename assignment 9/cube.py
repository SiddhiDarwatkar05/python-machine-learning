def cube(num):
    cube = num*num*num
    return cube

def main():
    value1 = int(input("Enter the number"))

    Ret = cube(value1)
    print("cube of number is:",Ret)
    

if __name__ == "__main__":
    main()
    