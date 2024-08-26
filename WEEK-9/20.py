# 20.Python Program Using map, filter, and lambda Functions 
# Write a Python program that utilizes the map, filter, and lambda functions to achieve the following 
# objectives: 
#   Use map to convert a list of integers to their corresponding squares. 
#   Use filter to keep only the squared numbers that are multiples of a specific number.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] #example
squares = list(map(lambda x: x ** 2, l))

specific_number = 5 #example
filtered_squares = list(filter(lambda x: x % specific_number == 0, squares))

print(filtered_squares)
