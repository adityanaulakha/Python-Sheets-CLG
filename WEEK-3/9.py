##9. Take integers N as input. Your task is to calculate and print the sum of the digits of the given
##number N.
##Input:- N = 1589
##Output:- 23
##Explaination:- For the number 1589, the digits are 1,5,8,9. The
##Sum(1589) = 1+5+8+9 = 23.

n=int(input("Enter the Number: "))
sum=0
while n!=0:
    last_digit=n%10
    sum=sum+last_digit
    n=n//10
print("The sum is: ",sum)
