import math
l = float(input("Enter the length of the  rectangle: "))
w = float(input("Enter the width of the rectangle: "))
rec_area = l * w 
print("Area of the rectangle: ",rec_area)
r = float(input("Enter the radius of the circle: "))
cir_area = r*r*math.pi 
print("Area of the circle: ",cir_area)
b = float(input("Enter the base of the triangle: "))
h = float(input("Enter the height of the triangle: "))
tri_area = 1/2 * b * h 
print("Area of the triangle: ",tri_area)