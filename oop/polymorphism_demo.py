import math  # needed for Circle area calculation

# Base class
class Shape:
    def area(self):
        # This method should be overridden in subclasses
        raise NotImplementedError("Subclasses must implement this method")

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
