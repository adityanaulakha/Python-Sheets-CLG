# 19.Convert Names to Lowercase Using Map and Lambda Function 
# Create a Python program that accomplishes the following tasks: 
#   Define a list names containing string values. 
#   Use the map() function with a lambda function to convert each name in the list names 
# to lowercase. 
#   Store the modified names in a variable result. 
#   Print the result list.

l = ['Aditya','Hero','Saket','Mihir']
l_new = list(map(lambda x: x.lower(),l))
print(l_new)