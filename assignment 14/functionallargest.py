large = lambda no1,no2,no3:no1 if no1>no2 & no1>no3 else (no2 if no2>no1 &no2>no3 else no3 ) 

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))

Ret = large(num1,num2,num3)

print("largest number  is:",Ret)