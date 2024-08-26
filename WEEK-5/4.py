##4. Search Element
##You are given array A and an integer B. You have to tell whether B is present in array A or
##not.
##Input:-
##N = 4
##A = 1 5 9 1
##5
##Output:
##1

A=[]
B=int(input("Enter the to be searched: "))
n=int(input("Enter the count of elements: "))
for i in range(0,n,1):
    ele=int(input("Enter the element of list: "))
    A.append(ele)
key_found= False
for ele in A:
    if ele==B:
        key_found=True
        break
if key_found==True:
    print(f"The Key is found at {A.index(ele)+1}")
else:
    print("The Key is not found.")
