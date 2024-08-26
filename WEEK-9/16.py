# 16.Filter Even No 
# Write a Python program that defines a function fun(a) which takes an integer a as input and 
# returns True if a is even, otherwise it returns False. Then, create a list called sequence containing 
# integers and floating-point numbers. Use the filter() function along with the fun function to 
# filter out the even numbers from the sequence list, and store the filtered values in a new list 
# called filtered. Finally, print the filtered list.

a = int(input())
def fun(a):
    if a%2==0:
        return True
    else:
        return False
sequence = [32,15,14,10,7,3,4,8,24.12,122.12]
sequence_new = list(filter(fun,sequence))
print(sequence_new)