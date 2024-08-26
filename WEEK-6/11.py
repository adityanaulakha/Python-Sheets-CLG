# 11.Isalnum()
# You are given a function isalpha() consisting of a character array A.
# Print 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else,
# print 0.
# A = ["P" , "y", "t", "h", "O" , "n", "2" , "4"]
# Output:
# 1
# A = ["P" , "y", "t", "h", "O" , "n", "2" , "4"]

l = []
n=int(input("Enter the count of elements: "))
for i in range(n):
    l.append(input())
for i in l:
    if i.isalnum():
        print(1)
        break
    else:
        print(0)
        break