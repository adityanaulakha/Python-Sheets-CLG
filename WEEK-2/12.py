##You are given 3 integer angles(in degrees) A, B and C of a triangle. You have to tell
##whether the triangle is valid or not.A triangle is valid if sum of its angles equals to 180.

a=int(input("Enter the first angle: "))
b=int(input("Enter the second angle: "))
c=int(input("Enter the third angle: "))
if a+b+c==180:
    print("The triangle is valid")
elif a+b+c!=180:
    print("The triangle is not valid")
