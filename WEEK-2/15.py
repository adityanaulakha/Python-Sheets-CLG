##Accept the percentage from the user and display the grade
##according to the following criteria.
##● Below 25 – D
##● 25 to 45 – C
##● 45 to 65 – B
##● 65 to 85 – A
##● Above 85 – A+

per=int(input("Enter your percentage: "))
if per>=85:
    print("Your grade is: A+")
elif per<85 and per>=65:
    print("Your grade is: A")
elif per<65 and per>=45:
    print("Your grade is: B")
elif per<45 and per>=25:
    print("Your grade is: C")
elif per<25 :
    print("Your grade is: D")
