# 6.Volume Of Sphere 
#  You are given a positive integer A denoting the radius of a sphere. You have to calculate the  volume of the sphere.  
# Volume of a sphere having radius R is given by (4 * π * R^3) / 3.  NOTE: Since, the answer can be a real number, you 
# have to return the ceil value of the  volume. 
# Ceil value of a real number X is the smallest integer that is greater than or equal to  X

import math
def vol(A):
    c = 4*math.pi*A**3
    return math.ceil(c)
A = int(input())
print("Volume of Sphere:",vol(A))