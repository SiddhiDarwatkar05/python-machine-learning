div = lambda num:(num%3==0 &num%5==0)

def main():

    num = list(map(int,input("enter numbers with space:").split()))

    Ret = list(filter(div,num))

    print("numbers divisible by 3 & 5 are:",Ret)

if __name__ == "__main__":
    main()