WAP to define and utilize a Python function named introduce to print out information about 
individuals, including their name, age, and profession, with an optional default value for the 
profession parameter

def introduce(name, age, profession="Student"):
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

name = input("Enter name: ")
age = input("Enter age: ")
profession = input("Enter profession (optional): ")

if profession.strip():
    introduce(name, age, profession)
else:
    introduce(name, age)

