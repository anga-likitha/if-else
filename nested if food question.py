""" Take two user inputs one as day and one as meal time. Show the following
table using nested if statements :
1. day = Monday
Breakfast = Poori Sabzi
Lunch = Sambhar Rice
Dinner = Chicken Rice
2. Day = Tuesday
◦ Breakfast = Poha
◦ Lunch = Rajma Rice
◦ Dinner = Roti Sabzi"""
day=input("enter the day")
meal_time=input("enter the meal_time")
if day=='monday' :
    if meal_time=='Breakfast':
        print("Poori Sabzi")
    elif meal_time=='Lunch':
        print("Sambhar Rice")
    elif meal_time=='Dinner':
        print("Chicken Rice")
elif day=='Tuesday' :
    if meal_time=='Breakfast':
        print("Poha")
    if meal_time=='Lunch':
        print("Rajma Rice")
    if meal_time=='Dinner':
        print("Roti Sabzi")