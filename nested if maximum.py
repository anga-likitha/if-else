num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
num3=int(input("enter the number:"))
if(num1>num2):
    if(num1>num3):
        print("num2,maximum")
    else:
        print("num2,is grater")
elif(num2<num1):
    if(num2>num3):
        print("num1,maximum")
    else:
        print("num1,is maxium")
else:
    if(num3<num2):
        print("num2,is maxium")
    else:
        print("num2,is grater")
        
        