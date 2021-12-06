num1=int(input("enter the rooms:"))
num2=int(input("enter the girls:"))
num3=int(input("enter the beds:"))
if(num1==102):
        print("this is apparent room. you go another room")
elif(num1==204):
        print("team leaders room.you go another room")
elif(num1==101):
        print("programme manager room.you go to another room")
elif(num1==202):
        print("this is kitchen room .go to another room")
elif(num1==104):
    if(num3>=num2):
        print(num3-num2,"girls is less.shift this room")
    else:
        print(num2-num3,"beds is less.shift this room")
elif(num1==304):
    if(num2<=num3):
        print(num3-num2,"girls less.shift this room")
    else:
        print(num2-num3,"beds is less.shift the room")
elif(num1==303):
    if(num3<=num2):
        print(num2-num3,"beds is less.shift this room")
    else:
        print(num3-num2,"girls is less.shift thi room")
else:
    if(num1==103):
        if(num3>=num2):
            print(num3-num2,"girls is less.shift this room")
        else:
            print(num2-num3,"beds is less .shift this room")
        
    

        
              