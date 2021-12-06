time=int(input("enter the time:"))
day_timing=(input("enter the day_timing:"))
if day_timing=="morning":
    if time>=6 and time<8:
        print("exercise time,fresh")
    if time>=8 and time<1:
        print("coding")
    else: print("playing")
if day_timing=="afternoon":
    if time>=1 and time<2:
        print("lunch")
    if time>=2 and time<4:
        print("second coding")
if day_timing=="evening":
    if time>=4 and time<6:
        print("snacks")
    if time>=6 and time<8:
        print("english activity")
if day_timing=="night":
    if time>=8 and time<9:
        print("dinner")
    if time>=9 and time<12:
        print("sleep")
    else:
        print("our wish")


        
