# WAP to check the number is divisible by 7 or last digit is 5.

n=int(input("Enter the number: "))
last_digit=n%10
if last_digit%5==0 or n%7==0:
    print("The number is divisible by 7 or last digit is 5")
    
