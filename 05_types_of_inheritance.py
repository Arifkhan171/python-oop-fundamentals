# Types of Inheritance in Python
# 1. Single   - one parent, one child
# 2. Multilevel - grandparent → parent → child
# 3. Hierarchical - one parent, multiple children
# 4. Multiple - one child, multiple parents
# 5. Hybrid - combination of above types

# 1. Single Inheritance
class Animal:
    def breathe(self):
        print("Animal breathes")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.breathe()
d.bark()

# 2. Multilevel Inheritance
class Product:
    def review(self):
        print("Product review")

class Phone(Product):
    def buy(self):
        print("Buy phone")

class SmartPhone(Phone):
    def features(self):
        print("Smartphone features")

sm = SmartPhone()
sm.review()
sm.buy()
sm.features()

# 3. Hierarchical Inheritance
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car drives")

class Bike(Vehicle):
    def ride(self):
        print("Bike rides")

car = Car()
bike = Bike()
car.start()
bike.start()

# 4. Multiple Inheritance
class A:
    def method_a(self):
        return 20

class B:
    def method_b(self):
        return 30

class C(A, B):
    def method_c(self):
        return self.method_a() + self.method_b()

obj = C()
print(obj.method_c())

# 5. Multilevel with super
class A:
    def m1(self):
        return 20

class B(A):
    def m1(self):
        return super().m1() + 30

class C(B):
    def m1(self):
        return super().m1() + 70

obj = C()
print(obj.m1())   # 20 + 30 + 70 = 120
