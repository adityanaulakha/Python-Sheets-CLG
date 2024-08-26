##1.Sum of list
##Given an array compute the sum of all elements.
##Input :-
##A = [1,2,3,4,5]
##Output:
##15

A=[]
n=int(input("Enter the count of elements you want in the list: "))
for i in range(0,n,1):
    ele=int(input("Enter the"+"element of list: "))
    A.append(ele)
print(sum(A,0))

