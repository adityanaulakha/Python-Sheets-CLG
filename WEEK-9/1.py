# 1.Keyword argument 
# Define a function in Python Introduce , providing their name, age, and profession as 
# arguments.

def introduce(name,age,profession):
    return name,age,profession

name = input()
age = int(input())
profession = input()

print(introduce(name,age,profession))