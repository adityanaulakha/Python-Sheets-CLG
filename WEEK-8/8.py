# 8.Sum the Array 
#  Write a program to print sum of elements of the input array A of size N.

def sum(A):
    summ = 0
    for i in A:
        summ += i
    return summ
A = list(map(int,input("Enter the array: ").split()))
print("Sum:",sum(A))