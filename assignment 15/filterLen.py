check = lambda word:len(word)>5

def main():
    word = input("enter words separated by space:").split()

    Ret = list(filter(check,word))

    print("string greater than length 5 is:",Ret)

if __name__ == "__main__":
    main()