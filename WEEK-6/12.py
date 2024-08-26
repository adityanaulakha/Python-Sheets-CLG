# 12.Isalpha() 
# You are given a function isalpha() consisting of a character array A.Print 1 if all the characters of the 
# character array are alphabetical (a-z and A-Z), else print 0. 

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