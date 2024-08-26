# 10.toupper()
# You are given a function to_upper() consisting of a character array A.
# Convert each character of A into Uppercase character if it exists. If the Uppercase of a
# character does not exist, it remains unmodified.
# The lowercase letters from a to z is converted to uppercase letters from A to Z respectively.
# Print the uppercase version of the given character array.
# Input:
# A = ["s" , "U", "y", "A", "s" , "H"]
# Output:
# ["S" , "U", "Y", "A", "S" , "H"]

l=[]
n=int(input("Enter the Count of elements: "))
for i in range(n):
    l.append(input())
for i in range(len(l)):
    if l[i].islower():
        l[i]=l[i].upper()
print(l)
