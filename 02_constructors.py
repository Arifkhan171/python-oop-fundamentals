# Constructors in Python OOP
# __init__ is a special method (magic method) that runs automatically
# when an object is created. Used to initialize object attributes.

# what is self:
# self refers to the current object calling the method.
# When you call obj.method(), Python passes obj as self automatically.

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

s1 = Student("Arif", 3.8)
s2 = Student("Ajab", 3.5)

print(s1.name, s1.gpa)
print(s2.name, s2.gpa)


# constructor with default values
class Student:
    def __init__(self, name="Unknown", gpa=0.0):
        self.name = name
        self.gpa = gpa

s3 = Student()
print(s3.name, s3.gpa)  # Unknown 0.0
