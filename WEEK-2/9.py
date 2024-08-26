##WAP to check whether an year is a leap year or not.

year=int(input("Enter the year: "))
if year%4==0:
    if year%400 or year%100!=0:
        print("Leap Year")
elif year%4!=0:
    print("Not a Leap Year")
