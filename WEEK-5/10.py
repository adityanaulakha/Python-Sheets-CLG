##10. Reverse
##Given an array A, Find the reverse of it.
##Input:
##A = [3, 5, 1, 2, 1, 2]
##Output:
##[2, 1, 2, 1, 5, 3]

##Method 1:
A=[]
n=int(input("Enter the count of elements: "))
print("Enter the elements of list: ")
for i in range(0,n,1):
    ele=int(input())
    A.append(ele)
A.reverse()
print(A)

##Method 2:
A=[]
Reverse_A=[]
n=int(input("Enter the count of elements: "))
print("Enter the elements of list: ")
for i in range(0,n,1):
    ele=int(input())
    A.append(ele)
Reverse_A= A[::-1]
print(Reverse_A)

##Method 3:
A=[]
Reverse_A=[]
n=int(input("Enter the count of elements: "))
print("Enter the elements of list: ")
for i in range(0,n,1):
    ele=int(input())
    A.append(ele)
Reverse_A= list(reversed(A))
print(Reverse_A)
