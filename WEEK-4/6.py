##6.
##*_ _ _ _ _*
##*_ _ _ _*
##*_ _ _*
##*_ _*
##*_*
n=int(input("Enter the rows:"))
for i in range(n, 2, -1):
    for j in range(i):
        if j == 0 or j == i-1:
            print("*", end=" ")
        else:
            print("_", end=" ")
    print()

