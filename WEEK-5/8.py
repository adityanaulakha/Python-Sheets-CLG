##8.Square of Array
##You are provided with an integer array A. Return another array B of size same as that of A
##such that B[i] = A[i]^2
##Input:
##A=[2, 6, 8, 1]
##Output:
##[4, 36, 64, 1]

A=[]
B=[]
n=int(input("Enter the count of elements: "))
print("Enter the elements of list: ")
for i in range(0,n,1):
    ele=int(input())
    A.append(ele)
for ele in A:
    ele_B=(ele)**2
    B.append(ele_B)
print("A=",A)
print("B=",B)
