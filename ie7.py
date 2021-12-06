language=(input ("enter the language="))
if language=="english":
     print("welcome to central bank of india\nswip your card=")
     balance=50000
     print("chose your transection\n1.balance enquary\n2.withdraw money\n3.deposit\n4.transfer money\n6.exit")
transaction=input("enter the transection=")
if transaction=="balance enquary":
    swipe=input("do you want swipe your card=")
    if swipe=="yes":
        atmpin=5678
    pin=int(input("enter your pin="))
    if pin==atmpin:
        print("swipe your card\n thankyou for using me ")
else:
    print("wrong pin") 
    eliftransaction=="withdraw money"
atmpin=5678
pin=int(input("enter your pin="))
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