from math import pi

radius = float(input("Enter the radius of the sphere: "))

# area of sphere = 4 * pi * r^2
area = 4 * pi * radius ** 2

print(f"The area of sphere with radius {radius} is {"{:2f}".format(area) if area < 1e6 else  "{:e}".format(area)}.")