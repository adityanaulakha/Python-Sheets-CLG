##Write a program to input three numbers(A, B & C) from user and
##print the minimum element among A, B & C.

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a<b and a<c:
    print("The minimum is:",a)
elif b<a and b<c:
    print("The minimum is:",b)
elif c<a and c<b:
    print("The minimum is:",c)
