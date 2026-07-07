def check(no):
    if no%5 == 0:
        return True
    else:
        return False


def main():
    num = int(input("enter a number:"))
    ret = check(num)
    print(ret)

if __name__ == "__main__":
    main()