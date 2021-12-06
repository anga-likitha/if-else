num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
num3=int(input("enter the number:"))
if(num1>num2):
    if(num1>num3):
        print("num1 is grater")
    else:
        print("num1,is less")
elif(num2>num3):
    if(num2<num1):
        print("num2, is less")
    else:
        print("num2,is grater")
else:
    if(num3<num1):
        print("num3 is less")
    else:
        print("num3,is grater")
    

