import math

def traoezid_area(h, a, b):
    return math.fsum([a, b]) * h / 2

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
print("Excpected Output: ", traoezid_area(h, a, b))