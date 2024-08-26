##5 .Write a program to find sum all Natural numbers from 1 to N where you have to take N as
##input from user
##Input:- N = 10
##Output:- 55

N=int(input("Enter the Number: "))
sum=0
for i in range(1,N+1,1):
    sum= sum+i
print(sum)
