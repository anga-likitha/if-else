num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
num3=int(input("enter the number:"))
if num1>num2 and num1>num3: 
    if(num2>num3):
        print(num2,"is 2nd maximum num")
    else:
        print("num3,is less" )
if num2>num3 and num2>num1:
    if num3>num1:  
        print(num3,"is 2nd maximum num")
    else:
        print("num1, is less")  
else:
    if num3>num2 and num3>num1:
        if(num2>num1):
            print(num2,"is 2nd gratest num")
        else:
            print(num1,"is less")
