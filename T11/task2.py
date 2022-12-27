import math

shape = input("what shape is the building? Square, Rectangular or Round: ")

if shape == "square":
    length = float(input("Enter the length of the side: "))
    area = length * length
    print("area of the foundation of the building: ", area)

elif shape == "rectangular":
    length = float(input("Enter the length of the side: "))
    weidth = float(input("Enter the weidth of the side: "))
    area = length * weidth
    print("area of the foundation of the building: ", area)

elif shape == "round":
    radius = float(input("Enter the radius of the building: "))
    area = math.pi * (radius * radius)
    print("area of the foundation of the building: ", area)