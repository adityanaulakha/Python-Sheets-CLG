# 18.1. Add 10 to Each Element of a List Using Map and Lambda Function 
# Create a Python program that accomplishes the following tasks: 
#   Define a list arr containing integer values. 
#   Use the map() function with a lambda function to add 10 to each element of the list 
# arr. 
#   Store the modified values in a variable ans. 
#   Print the ans list.

arr = [1,2,3,4,5,6,7,8,9,10]
ans = list(map(lambda x:x+10,arr))
print(ans)