## WAP to check if number last digit is 4.
n=int(input("Enter the number: "))
last_digit=n%10
if last_digit%4==0:
    print("The last digit of the number is 4")
else:
    print("The last digit of the number is not 4")
