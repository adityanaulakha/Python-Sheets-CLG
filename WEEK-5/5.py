##5. Negative Integers
##Write a program to print all negative numbers from input array A of size N.
##Input:-
##N = 5
##A = 1 -5 2 -8 -4
##Output:
##-5
##-8
##-4

A=[]
n=int(input("Enter the count of elements: "))
print("Enter the elements of list: ")
for i in range(0,n,1):
    ele=int(input())
    A.append(ele)
print("The Negative elements are:")
for ele in A:
    if ele<0:
        print(ele)


##                   OR
##
##A=[]
##negative_num=[]
##n=int(input("Enter the count of elements: "))
##print("Enter the elements of list: ")
##for i in range(0,n,1):
##    ele=int(input()) 
##    if ele<0:
##        negative_num.append(ele)
##    else:
##        A.append(ele)
##print("The negative numbers are: ",negative_num)
##print("The non-negative numbers are: "A)
