## Read three integers and print their maximum.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a>b and a>c:
    print("The maximum number is: ",a)
if a<b and b>c:
    print("The maximum number is: ",b)
if c>b and b<c:
    print("The maximum number is: ",c)
