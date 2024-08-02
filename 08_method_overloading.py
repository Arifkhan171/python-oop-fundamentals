# Method Overloading in Python OOP
# Python does not support true method overloading (same name, different args).
# Last defined method with same name overrides previous ones.
# Solution: use default arguments to simulate overloading.

class Geometry:
    def area(self, a, b=0):
        if b == 0:
            print(f"Circle area: {3.14 * a * a:.2f}")
        else:
            print(f"Rectangle area: {a * b}")

g = Geometry()
g.area(5)       # circle
g.area(5, 3)    # rectangle


# another approach using *args
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(1, 2))         # 2 arguments
print(calc.add(1, 2, 3))      # 3 arguments
print(calc.add(1, 2, 3, 4))   # 4 arguments
