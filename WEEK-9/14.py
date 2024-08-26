# 14.Max of two No. 
# Write a Python program that defines a lambda function called Max that takes two parameters 
# a and b, and returns the maximum of the two values. Then, call the lambda function Max with 
# the values 1 and 2, and print the result obtained from the call in a single line of code.

Max = lambda a, b: a if a > b else b
result = Max(1, 2)
print(result)