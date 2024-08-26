##3 .Write a program to print all even numbers from 1 to N where you have to take N as input from
##the user.
##Input:- N = 10
##Output:- 2 4 6 8 10

N=int(input("Enter the Number: "))
for i in range(2,N+1,2):
    print(i,end=" ")
