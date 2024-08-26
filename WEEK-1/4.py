##Write a program that takes a user's age as input and
##determines if they are eligible to vote (above 18)
age=int(input("Enter the age: "))
if age>=18:
    print("Eligible to Vote")
elif age<18:
    print("Not Eligible to Vote")
