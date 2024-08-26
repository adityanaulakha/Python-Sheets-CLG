# 15.Max of three No. 
# Create a Python program that accomplishes the following tasks: 
#   Define a lambda function max_of_three that takes three parameters a, b, and c, and 
# returns the maximum of the three values. 
#   Call the lambda function max_of_three with three integer values. 
#   Print the result obtained from calling the lambda function. 
# NOTE:- Try to Solve this question with if-else.

MAX = lambda a,b,c: a if a>b and a>c else b if b>a and b>c else c
result = MAX(a = int(input()),b = int(input()),c = int(input()))
print(result)