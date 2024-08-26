# 18.Filter Numbers Greater Than 60 
# Write a single line of Python code that accepts a list of integer values from the user, filters 
# out the numbers greater than 60 using the filter() function with a lambda function, and stores 
# the filtered values in a variable ans. Print the ans list

ans = list(filter(lambda x: x > 60, map(int, input().split())))
print(ans)