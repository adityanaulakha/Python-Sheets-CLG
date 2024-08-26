##3. Max and Min of an Array
##Take input an array A of size N and write a program to print maximum and minimum
##elements of the input array .Here N represents the length of the array .
##Input :-
##N = 5
##A = 1 2 3 4 5
##Output:
##5 1

A=[]
n=int(input("Enter the count of elements: "))
for i in range(0,n,1):
    ele=int(input("Enter the element of list: "))
    A.append(ele)
print(max(A),min(A),end=" ")

