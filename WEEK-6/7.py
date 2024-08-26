# 7.First Occurrence
# You are given a character string A, having length N and an integer ASCII code B.
# You have to tell the leftmost occurrence of the character having ASCII code equal to B, in A
# or report that it does not exist.
# Input:
# A = "aabbcc"
# B = 98
# Output:
# 2

s=input("Enter the String: ")
b=int(input("Enter the ASCII value of the Key: "))
for i in range(len(s)):
    if ord(s[i])==b:
        index=i
        break
print(index)

# OR 

# for i, char in enumerate(s):
#     if ord(char)==b:
#         print(i)
#         break
