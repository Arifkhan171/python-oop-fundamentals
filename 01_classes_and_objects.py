# OOP in Python - Classes and Objects
# A class is a blueprint. An object is a real instance of that blueprint.
# Class name: PascalCase | Method/variable name: snake_case

class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 500001
        self.menu()

    def menu(self):
        user_input = input("""
        Hello, what do you want?
        1. Create PIN
        2. Deposit
        3. Withdraw
        4. Check Balance
        5. Exit
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Goodbye")

    def create_pin(self):
        self.pin = input("Enter your PIN: ")
        print("PIN set successfully")

    def deposit(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            amount = int(input("Enter amount to deposit: "))
            self.balance += amount
            print("Deposited successfully")
        else:
            print("PIN mismatch")

    def withdraw(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} withdrawn successfully")
            else:
                print("Insufficient balance")
        else:
            print("Invalid PIN")

    def check_balance(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            print(f"Your balance is {self.balance}")
        else:
            print("Invalid PIN")


# obj = Atm()  # uncomment to run the ATM simulation
