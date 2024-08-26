##1. Write a program that takes a positive integer N as input from the user and
##prints all natural numbers from 1 to N, with each number followed by a space.
##Input:- N = 5
##Output:- 1 2 3 4 5

N=int(input("Enter the Number: "))
for i in range(1,N+1):
    print(i,end=" ")
