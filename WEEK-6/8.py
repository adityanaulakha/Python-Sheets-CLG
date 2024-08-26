# 8.First Occurrence Of Word
# You are given two character strings A and B.
# You have to find the first occurrence of string B in string A, as a substring, and return the
# starting position of first occurrence.
# A substring is a contiguous sequence of characters within a string. For e.g "at" is a substring
# in "catalogue".
# Input:
# A = "aabababaa"
# B = "ba"
# Output:
# 2

a = input("Enter the String: ")
b = input("Enter the substring: ")
c = a.find(b) 
print(c)