# Method Overriding and super() in Python OOP
# Method overriding: child class defines method with same name as parent.
# Child method runs instead of parent method.
# super(): calls the parent class method from inside child class.

class Teacher:
    def study(self):
        print("Teacher studies books")

class Student(Teacher):
    def study(self):
        print("Student studies books")

obj = Student()
obj.study()     # Student method runs due to overriding

# using super() to call parent method alongside child method
class Teacher:
    def study(self):
        print("Teacher studies books")

class Student(Teacher):
    def study(self):
        super().study()          # parent method runs first
        print("Student studies books")

obj = Student()
obj.study()

# overriding constructor with super()
class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num

class Child(Parent):
    def __init__(self, num, val):
        super().__init__(num)    # parent constructor called
        self.__val = val

    def get_val(self):
        return self.__val

c = Child(100, 200)
print(c.get_num())
print(c.get_val())
