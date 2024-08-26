##2. Copy the Array
##You are given a constant array A and an integer B.
##You are required to return another array where Arr[i] = A[i] + B.
##Input :-
##A = [1,2,3,2,1]
##B = 3
##Output:
##[4,5,6,5,4]

A=[]
n=int(input("Enter the count of elements: "))
for i in range(0,n,1):
    ele=int(input("Enter the element of list: "))
    A.append(ele)
B= A.copy()
C=int(input("Enter NUMBER to be added: "))
for i in range(len(A)):
    A[i]=A[i]+C
print("The Original List was:",B)
print("The New List is: ",A)
 
