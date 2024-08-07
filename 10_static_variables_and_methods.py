# Static Variables and Methods in Python OOP
# Static variable: shared across all objects (class level)
# Instance variable: unique to each object
# Static method: does not depend on any object or instance

class Atm:
    __counter = 1    # private static variable shared by all objects

    def __init__(self):
        self.pin = ""
        self.balance = 50000
        self.sno = Atm.__counter     # fixed: was Atm.counter (wrong)
        Atm.__counter += 1

    @staticmethod
    def get_counter():
        return Atm.__counter

    @staticmethod
    def set_counter(new):
        if isinstance(new, int):
            Atm.__counter = new
        else:
            print("Invalid value — must be integer")

    def create_pin(self):
        self.pin = input("Enter PIN: ")
        print("PIN set successfully")

    def check_balance(self, pin):
        if pin == self.pin:
            print(f"Balance: {self.balance}")
        else:
            print("Invalid PIN")


obj1 = Atm()
obj2 = Atm()
obj3 = Atm()

print("Serial numbers:", obj1.sno, obj2.sno, obj3.sno)
print("Counter value:", Atm.get_counter())

Atm.set_counter(10)
print("Counter after set:", Atm.get_counter())


# simple static method example
class MathUtils:
    @staticmethod
    def percentage(marks, total):
        return (marks / total) * 100

    @staticmethod
    def is_pass(marks, passing=33):
        return marks >= passing

print(MathUtils.percentage(85, 100))
print(MathUtils.is_pass(25))
