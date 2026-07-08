import Arithmetic

def main():
    num1 = int(input("enter first number:"))
    num2 = int(input("enter second number:"))

    print("addition is:",Arithmetic.Add(num1,num2))

    print("subtraction is:",Arithmetic.Sub(num1,num2))

    print("multiplication is:",Arithmetic.Mult(num1,num2))
    
    print("division is:",Arithmetic.Div(num1,num2))
    

if __name__ == "__main__":
    main()