# 12.Square of that integer using a lambda function 
 
# You want to create a Python program that takes an integer input, calculates the square of that 
# integer using a lambda function, and then prints the result. 
 
# Input :  
#    a= 4 
# Output: 
# 16

number = int(input())
square = lambda number: number**2
print(square(number))