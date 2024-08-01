# Abstraction in Python OOP
# Forces child classes to implement specific methods.
# Rules:
# 1. Cannot create object of abstract class
# 2. Every child class MUST implement all abstract methods
# Non-abstract methods in abstract class are optional to override.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def description(self):     # not abstract — optional to override
        print("I am a shape")

class Triangle(Shape):
    def area(self):            # mandatory
        print("Triangle area = 0.5 * base * height")

    def perimeter(self):       # mandatory
        print("Triangle perimeter = a + b + c")

class Circle(Shape):
    def area(self):
        print("Circle area = 3.14 * r * r")

    def perimeter(self):
        print("Circle perimeter = 2 * 3.14 * r")

t = Triangle()
t.area()
t.perimeter()
t.description()

c = Circle()
c.area()

# this would raise TypeError — cannot instantiate abstract class
# s = Shape()
