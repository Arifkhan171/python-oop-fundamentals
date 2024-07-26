# Polymorphism in Python OOP
# poly = many, morph = forms
# Same method name behaves differently in different classes.
# Combines inheritance and method overriding.

class Shape:
    def area(self):
        print("Shape area not defined")

class Triangle(Shape):
    def area(self):
        print("Triangle area = 0.5 * base * height")

class Rectangle(Shape):
    def area(self):
        print("Rectangle area = length * width")

class Circle(Shape):
    def area(self):
        print("Circle area = 3.14 * r * r")

# polymorphism in action — same method, different behavior
shapes = [Triangle(), Rectangle(), Circle()]
for shape in shapes:
    shape.area()

# real example with calculations
class Triangle:
    def area(self, base, height):
        return 0.5 * base * height

class Rectangle:
    def area(self, length, width):
        return length * width

class Circle:
    def area(self, radius):
        return 3.14 * radius * radius

shapes = [Triangle(), Rectangle(), Circle()]
args   = [(6, 4), (5, 3), (7,)]

for shape, arg in zip(shapes, args):
    print(f"{shape.__class__.__name__} area: {shape.area(*arg)}")
