# 5.Write a Python program that imports the random module to perform random number  generation and selection operations.
# Print the following results: 
# 1.   Generate a random integer between 0 and 5 (inclusive) using the randint() function.
# 2.   Generate a random floating-point number between 0 and 1 using the random() function.
# 3.   Generate a random floating-point number between 0 and 100 using the random() function and  scaling.
# 4.   Select a random element from the given list [1, 4, True, 800, "python", 27, "hello"] using the  choice() function.

import random as r
print(r.randint(0,5))
print(r.random())
print(r.random() * 100)
print(r.choice([1, 4, True, 800, "python", 27, "hello"]))