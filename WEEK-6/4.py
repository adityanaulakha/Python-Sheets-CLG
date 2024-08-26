# 4.Trim From Ends
# You are given a character string A. You to trim(remove) both leading and trailing asterisk
# characters('*') in the string and return the resultant string.
# Input:
# A = "**h*e*l*lo*"
# Output:
# h*e*l*lo

s=input("Enter the String: ")
for i in range(len(s)):
    if s[i].isalnum():
        s = s[i:]
        break
for i in range(len(s)-1,-1,-1):
    if s[i].isalnum():
        s = s[:i+1]
        break
print(s)
