##10. You are given an integer A as input and you need to determine whether it is a palindrome or
##not.A palindrome integer is one whose digits, when reversed, result in the same number.
##For example, 121 is a palindrome because its reverse is also 121, but 123 is not a palindrome
##because its reverse is 321.Note: The given integer will not have any leading zeros.

a=int(input("Enter the Number: "))
temp=a
reverse=0
while temp>0:
    remainder= temp%10
    reverse= (reverse*10)+remainder
    temp= temp//10
if reverse==a:
    print("The number is Palindrome.")
else:
    print("The number is not Palindrome.")
