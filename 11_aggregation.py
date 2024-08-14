# Aggregation in Python OOP
# Aggregation is a "has-a" relationship between classes.
# One class contains a reference to another class as an attribute.
# The contained object can exist independently outside the container.
# Aggregation is different from inheritance (is-a relationship).

class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def start(self):
        print(f"Engine started — {self.horsepower}hp {self.fuel_type}")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine    # Car HAS-A Engine (aggregation)

    def drive(self):
        self.engine.start()
        print(f"{self.brand} is now driving")

# Engine exists independently
engine = Engine(150, "Petrol")
car = Car("Toyota", engine)
car.drive()

# same engine can be used in another car
car2 = Car("Honda", engine)
car2.drive()


# another example — University and Department
class Department:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Department: {self.name}")

class University:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments   # University HAS-A list of Departments

    def show_departments(self):
        print(f"\n{self.name} departments:")
        for dept in self.departments:
            dept.info()

cs = Department("Computer Science")
ee = Department("Electrical Engineering")
bba = Department("Business Administration")

uni = University("University of Loralai", [cs, ee, bba])
uni.show_departments()
