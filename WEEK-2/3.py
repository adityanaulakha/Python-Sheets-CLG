## WAP to check the number is divisible by 3 and last digit is 4.

n=int(input("Enter the number: "))
last_digit=n%10
if last_digit%4==0 and n%3==0:
    print("The last digit of the number is 4")
    print("The number is divisible by 3")
elif last_digit%4!=0 and n%3==0:
    print("The last digit of the number is not 4")
    print("The number is divisible by 3")
elif last_digit%4==0 and n%3!=0:
    print("The last digit of the number is 4")
    print("The number is not divisible by 3")
elif last_digit%4!=0 and n%3!=0:
    print("The last digit of the number is not 4")
    print("The number is not divisible by 3")
    
