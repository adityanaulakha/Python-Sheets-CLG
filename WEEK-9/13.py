# 13.Odd and Even No 
# Write a Python program that performs the following tasks: 
#   Accepts an integer input from the user and stores it in a variable num. 
#   Defines a lambda function even_odd_No that takes one parameter num and returns 
# "even" if num is even, otherwise it returns "odd". 
#   Calls the lambda function even_odd_No with the input num and prints the result. 
# Provide the Python code to implement the above requirements.

num = int(input())
even_odd_No = lambda num: "Even" if num%2==0 else "Odd"
result = even_odd_No(num)
print(result)