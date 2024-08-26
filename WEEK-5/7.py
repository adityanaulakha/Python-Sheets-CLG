##7.Separate Odd Even
##You are given an integer array A.
##You have to print the odd and even elements of array A in 2 separate lines.
##Input:
##1 2 3 4 5
##Output:
##1 3 5
##2 4

A=[]
n=int(input("Enter the count of elements: "))
print("Enter the elements of list: ")
for i in range(0,n,1):
    ele=int(input())
    A.append(ele)
print("Odd Elements:")
for ele in A:
    if ele%2!=0:
        print(ele,end=" ")
print()
print("Even Elements:")
for ele in A:
    if ele%2==0:
        print(ele,end=" ")
