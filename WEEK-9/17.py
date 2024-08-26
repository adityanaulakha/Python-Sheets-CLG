# 17. Filter Even No with lambda fucntion 
# Create a Python program that accomplishes the following tasks: 
#   Define a list arr containing integer values. 
#   Use the filter() function with a lambda function to filter out the even numbers from the 
# list arr. 
#   Store the filtered values in a variable ans. 
#   Print the ans list.

l = [1,421,213,212,22,46,84,22]
ans = []
even = lambda i: i if i%2==0 else 0
result = list(filter(even,l))
print(result)