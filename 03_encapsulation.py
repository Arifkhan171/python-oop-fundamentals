# Encapsulation in Python OOP
# Hiding internal data to protect it from outside access.
# Types of variables:
# public   → accessible from anywhere (default)
# protected → convention only, prefix _ (warning outside class)
# private  → prefix __, blocked outside class

# public variable
class Phone:
    def __init__(self, brand):
        self.brand = brand       # public

p = Phone("Samsung")
print(p.brand)                   # accessible directly

# protected variable
class Phone:
    def __init__(self, brand):
        self._brand = brand      # protected (convention only)

p = Phone("Samsung")
print(p._brand)                  # accessible but not recommended

# private variable + getter and setter
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # private

    def get_balance(self, pin):
        if pin == "1234":
            return self.__balance
        return "Invalid PIN"

    def set_balance(self, pin, amount):
        if pin == "1234" and isinstance(amount, int):
            self.__balance += amount
            print("Balance updated")
        else:
            print("Invalid PIN or amount")

account = BankAccount(50000)
print(account.get_balance("1234"))
account.set_balance("1234", 10000)
print(account.get_balance("1234"))
