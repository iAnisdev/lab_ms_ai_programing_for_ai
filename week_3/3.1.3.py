from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2
    
    def calculate_circumference(self):
        return 2 * pi * self.radius
    

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_circumference())
    