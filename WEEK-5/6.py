##6 . Even Odd Elements
##For array A, you have to find the value of absolute difference between the counts of even
##and odd elements in the array.
##Input:
##1 2 3 4
##Output:
##0

A=[]
even_count=0
odd_count=0
n=int(input("Enter the count of elements: "))
print("Enter the elements of list: ")
for i in range(0,n,1):
    ele=int(input())
    A.append(ele)
for ele in A:
        if ele%2!=0:
            odd_count+=1
        elif ele%2==0:
            even_count+=1
diff= even_count - odd_count
if diff<0:
    diff= -(diff)
    print(diff)
else:
    print(diff)

            
