# 1.Square root of a number 
#  Given a number A. Return square root of the number if it is perfect square otherwise return  -1.
# Note: A number is a perfect square if its square root is an integer.

def sqrt(a):
    c = a**0.5
    if c.is_integer():
        return int(c)
    else:
        return -1
a = int(input())
print("Square Root is:",sqrt(a))