# 8.Write a Python program that uses the time module to introduce a delay of 1 second between printing consecutive numbers from 0 to 3.

import time as t
for i in range(4):
    print(i)
    t.sleep(1)