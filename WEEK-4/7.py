##7.
##_ _ _ _ *
##_ _ _ * *
##_ _ * * *
##_ * * * *
##* * * * *

n=int(input("Enter the number of line: "))
for i in range(1,n+1,1):
    print("_"*(n-i)+"*"*i)  
