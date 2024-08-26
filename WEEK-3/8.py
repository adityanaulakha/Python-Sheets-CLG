##8. Take integer N as input and Print the count of digits of that number.
##Input:- N = 10101
##Output:- 5
##Explaination:- 10101 has 5 digits

n=int(input("Enter the Number: "))
count=0
while n!=0:
    n=n//10
    count=count+1
print(count)
