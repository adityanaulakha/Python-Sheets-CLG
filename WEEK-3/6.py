##6 .You are given an integer A, you need to find and return the sum of all the even numbers
##between 1 and A. Even numbers are those numbers that are divisible by 2.
##Input:- A = 5
##Output:- 6
##Explaination:- Even numbers between [1, 5] are (2, 4).

a=int(input("Enter the Number: "))
sum=0
for i in range(1,a+1,1):
    if i%2==0:
        sum= sum+i
print(sum)
