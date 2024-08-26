# 7.Area Of Ellipse 
#  Given the lengths of semi-major axis A and semi-minor axis B of an ellipse, calculate the  Area of the Ellipse. 
# Area of ellipse having semi-major axis length a and semi-minor axis length b is given by π *  a * b. 
# NOTE: Since, the answer can be a real number, you have to return the ceil value of the area. 
# Ceil value of a real number X is the smallest integer that is greater than or equal to X

import math
def vol(A,B):
    c = math.pi*A*B
    return math.ceil(c)
A = int(input())
B = int(input())
print("Volume of Ellipse:",vol(A,B))