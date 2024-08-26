##Read Three angles of triangles and determine its types(Right traingle,Obtuse
##triangle,acute triangle).

a=float(input("Enter the first angle: "))
b=float(input("Enter the second angle: "))
c=float(input("Enter the third angle: "))
if a+b+c==90:
    print("The triangle is Right Angle Triangle")
if a+b+c>90:
    print("The triangle is Obtuse Triangle")
if a+b+c<90:
    print("The triangle is Acute Triangle")
