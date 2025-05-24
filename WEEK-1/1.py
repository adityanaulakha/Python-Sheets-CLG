#Write a program that converts a given number of days into weeks and days.


days=int(input("Enter the days: "))
weeks=days/7
left_days=days%7
print("The weeks are: ",int(weeks))
print("The days are: ",left_days)
    
