year=int(input("enter the year"))
if year%100==0:
    if year%400==0:
        print("leapyear")
    else:
        print("not a leapyear")
else:
    if year%4==0:
        print("leapyear")
    else:
        print("not a leapyear")
    