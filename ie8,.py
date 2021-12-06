atmpin=5678
pin=int(input("enter your pin="))
if pin==atmpin:
    print("swipe your card\n thankyou for using me ")
else:
    print("wrong pin")   
eliftransaction=="withdraw money"
amount=int(input("enter the balance="))
total=balance-amount
atm_pin=5678
pin=int(input("enter the pin"))
if pin==atm_pin:
    if amount<=balance:
        print(total)
        print("collect your cash\n thankyou for using me")
    else:
        print("you have no balance")    
elif transaction=="deposit":
    amount=int(input("enter the amount="))
    deposit=int(input("enter the amount="))
    total=amount+deposit
    atm_pin=5678
    pin=int(input("enter the pin"))
    if pin==atm_pin:
        if deposit>0:
            print(total)
            print("your deposit is successful\n thankyou for using me")
        else:
            print("worng pin") 
elif transaction=="transfer money":
    amount=int(input("enter the amount="))
    transfermoney=int(input("enter the amount transfer money="))
    total=amount-transfermoney
    atm_pin=5678
    pin=int(input("enter the pin"))
    if pin==atm_pin:
        if transfermoney>0:
            print(total)
            print("your money has been transfer\n thankyou for using me")
        else:
            print("worng pin") 
    else:
        print("pless enter valid amount")
elif transaction=="exit":
    exit=input("if you want exit enter yes=")
    if exit=="yes":
        atm_pin=5678
        pin=int(input("enter your pin"))
        if pin==atm_pin:
            print("exit")
        else:
            print("worng pin try again")
    else:
        print("chose any transection") 
else:
    print("language is not found")