def display(no):
    star = ""
    for i in range(no):
        star += " * " * no + "\n"    
    return star

def main():
    num = int(input("enter a number"))
    ret = display(num)
    print(ret)
          
if __name__ == "__main__":
    main()