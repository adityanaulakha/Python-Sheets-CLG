##11.
##**********
##****  ****
##***    ***
##**      **
##*        *
##*        *
##**      **
##***    ***
##****  ****
##**********

n=int(input("Enter the number of line: "))
for i in range(n,0,-1):
    print("*"*i+"  "*(n-i)+"*"*i)
for j in range(1,n+1,1):
    print("*"*j+"  "*(n-j)+"*"*j)
