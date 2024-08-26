# 9. tolower()
# You are given a function to_lower() which takes a character array A as an argument.
# Convert each character of A into lowercase characters if it exists. If the lowercase of a
# character does not exist, it remains unmodified.
# The uppercase letters from A to Z are converted to lowercase letters from a to z respectively.
# Print the lowercase version of the given character array.
# Input:
# A = ["S" , "u", "y", "A", "s" , "H"]
# Output:
# ["s" , "u", "y", "a", "s" , "h"]

l=[]
n=int(input("Enter the Count of elements: "))
for i in range(n):
    l.append(input())
for i in range(len(l)):
    if l[i].isupper():
        l[i]=l[i].lower()
print(l)
