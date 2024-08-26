##4.
##1
##1 *
##1 * 3
##1 * 3 *
##1 * 3 * 5
n=int(input("Enter the number of line: "))
for i in range(2,n+2,1):
    for j in range(1,i,1):
        if(j%2==0):
            print("*",end=" ")
        else:
            print(j,end=" ")
    print()
