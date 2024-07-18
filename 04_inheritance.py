# Inheritance in Python OOP
# Child class inherits attributes and methods from parent class.
# Private members cannot be inherited.

class Phone:
    def __init__(self, price, brand, model):
        self.price = price
        self.brand = brand
        self.model = model

    def buy(self):
        print(f"Buying {self.brand} phone for {self.price}")

class SmartPhone(Phone):
    def __init__(self, price, brand, model, os, ram):
        super().__init__(price, brand, model)
        self.os = os
        self.ram = ram

    def features(self):
        print(f"OS: {self.os} | RAM: {self.ram}")

sm = SmartPhone(30000, "Samsung", "Galaxy S21", "Android", "8GB")
sm.buy()
sm.features()
print(sm.brand)

# inheriting method from parent
class Teacher:
    def login(self):
        print("Teacher logged in")

    def register(self):
        print("Teacher registered")

class Student(Teacher):
    def enroll(self):
        print("Student enrolled")

student = Student()
student.login()      # inherited from Teacher
student.enroll()     # own method
