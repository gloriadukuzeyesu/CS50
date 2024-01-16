import sys

class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2


# p1 = Point(2,3)
# print(p1.x)
# print(p1.y)


#Decorattors. Used in Web applications 
def announce(f):
    def wrapper():
        print("About to run the functions")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hellofunction():
    print("Hello, Word")

# hellofunction()
    
#lamda functions

people = [
    {"name" : "Harray", "house" : "Gary"}, 
    {"name" : "Cho", "house" : "Revernclaw"}, 
    {"name" : "Draco", "house": "Slytherin"}, 
]


people.sort(key=lambda person: person["name"])


# print(people)
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)
try:
    z = x / y
    print(f"{x} / {y} = {z}")


except ZeroDivisionError:
    print("Error: Can not divide by 0.")
    sys.exit(1) #exit the program with error code 1. Meaning something went wrong















        
    