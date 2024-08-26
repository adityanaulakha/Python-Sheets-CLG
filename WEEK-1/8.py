##Area of Triangle Using Heron's Formula
##where sides entered by user.
a=int(input("Enter the side 1: "))
b=int(input("Enter the side 2: "))
c=int(input("Enter the side 3: "))
s= (a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**1/2
print("The Area is: ",area)
