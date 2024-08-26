# 1. Vowels vs Consonants
# Write a program to input T strings (S) from user and print count of vowels and consonants in
# it.
# Input:
# 2
# List
# Apple
# Output:
# 1 3
# 2 3

l=[]
n=int(input("Enter the Count of Elements: "))
print("Enter the elements: ")
for i in range(n):
    l.append(input())
for i in l:
    count_v=0
    for j in (i):
        if j in "aeiouAEIOU":
            count_v+=1
    print(count_v,len(i)-count_v)
