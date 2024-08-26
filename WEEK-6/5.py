# 5. Reverse string
# Write a program to reverse the words present in a string. Everything else should be preserved.
# Check example input/output. Note: There are no punctuation and special characters in the
# string.
# The string will only contain alphanumeric characters and spaces.
# Input:
# Everyone loves data science
# Output:
# enoyrevE sevol atad ecneics

s=input("Enter the String: ")
l=s.split()
l1=[i[::-1] for i in l]
s1=' '.join(l1)
print(s1)
