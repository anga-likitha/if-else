"""WRITE A PROGRAM FOR ATM"""
("ATM PROGRAM  ")
print("WEprintLCOME TO SBI ATM ")
print("SWIPE YOUR CARD HERE")
atm_pin=1234
pin=int(input("enter your atm pin :"))
transcation=["1","2","3","4","5","6"]
if pin==atm_pin :
    print("choose your transaction")
    print("1.Balance Enquiry")
    print("2.Withdraw Money")
    print("3.Deposit")
    print("4.change_Your_Pin")
    print("5.Transfer Money")
    print("6.Quit")
    trans=input("transcation :")
else:
    print("wrong pin enter again")
if trans=="1" :
    slip=input("do you want slip")
    if slip=="yes" :
        print("here is your slip")
    else:
        print("thanks for using sbi atm,visit again")
elif trans=="2" :
    amount=int(input("enter your amount"))
    if  amount>0 :
        print("collect your cash")
    else:
        print("no,balance")
elif trans=="3" :
    deposit=int(input("enter your amount to deposit"))
    if deposit >0 :
        print("deposited successfully")
    else:
        print("enter valid amount to deposit")
elif trans=="4" :
    Change_Your_Pin=int(input("enter your new pin"))
    if Change_Your_Pin!=pin:
        print("pin changed  successfully")
    else:
        print("enter valid pin to proceed")
elif trans=="5" :
    transfer=int(input("enter amount to transfer  :"))
    if        print" :
  >transfer0 :
    else:    else:

    Quit=in        print("transfered")
put(("enter correct amount")
    if Quit==elif trans=="6"press yes to quit")
"yes":
        print("quit")
    else:
        print("choose any question")
else:
    print("wrong transcaction")




"""
ATM PROGRAM  
WELCOME TO SBI ATM 
SWIPE YOU.R CARD HERE
enter your atm pin :1234
choose your transaction
1.Balance Enquiry
2.Withdraw Money
3.Deposit
4.hange_Your_Pin
5.Transfer Money
6.Quit
transcation :3.Deposit
enter your amount to deposit4567
enter your amount to deposit4567
deposited successfully


Global frame
atm_pin	1234
pin	1234
transcation	
 
trans	"3.Deposit"
deposit	4567
	
Objects
	
list
0	1	2	3	4	5
"1.Balance Enquiry"	"2.Withdraw Money"	"3.Deposit"	"4.Change Your Pin"	"5.Transfer Money"	"6.Quit"
"""