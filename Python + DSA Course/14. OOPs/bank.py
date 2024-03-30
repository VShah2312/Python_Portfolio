import random


class Bank:
    def __init__(self) -> None:
        self.acount_number = random.randint(100000, 999999)
        self.holder = input("Enter a name: ").title()
        self.balance = 0.0
        self.account_type = input("Enter a account type: ").title()

    def display(self) -> None:
        print(f"\nAccount number: {self.acount_number}")
        # Want to show only last four digits of account number
        # print(f"\nAccount number: {str(self.acount_number)[-4:]}")
        print(f"Account holder: {self.holder}")
        print(f"Account balance: {self.balance}")
        print(f"Account type: {self.account_type}\n")

    def withdraw(self) -> None:
        amt = float(input("Enter amount to withdraw: "))
        if amt < 0:
            print("Invalid amount")
            # return by itself to break out of function/method.
            return
        if self.balance >= amt:
            self.balance -= amt
            print(f"Updated balance = {self.balance}")
        else:
            print("Insuffciient Balance")

    def deposit(self) -> None:
        amt = float(input("Enter amount to deposit = "))
        if amt < 0:
            print("Invalid amount")
            return
        self.balance += amt

    def getBalance(self):
        print(f"Your balance ={self.balance}")


b1 = Bank()
b1.display()
b1.deposit()
b1.display()
b1.withdraw()
b1.display()
