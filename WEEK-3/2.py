##2. Write a program to print all Natural numbers from N to 1 where you have to take N as input
##from user.
##Input:- N = 5
##Output:- 5 4 3 2 1

N=int(input("Enter the Number: "))
for i in range(N,0,-1):
    print(i,end=" ")
