# 3.Is is Palindrome?
# Write a program to input T strings (S) from user and print 1 if it is palindrome otherwise print
# 0. NOTE:A string is palindrome if it reads the same from backward as from forward.
# Input:
# 3
# abcba
# axax
# abba
# Output:
# 1
# 0
# 1

l=[]
n=int(input("Enter the number of String: "))
print("Enter the Strings:")
for i in range(n):
    l.append(input())
for i in l:
    if i[::-1]==i:
        print(1)
    else:
        print(0)
