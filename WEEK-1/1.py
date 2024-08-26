#Write a program that converts a given number of days into weeks and days.


days=int(input("Enter the days: "))
if days%7==0:
    weeks=days/7
    left_days=days%7
    print("The weeks are: ",int(weeks))
    print("The days are: ",left_days)
elif days%7!=0:
    left_days=days%7
    weeks=days/7
    print("The weeks are: ",int(weeks))
    print("The days are: ",left_days)
    
