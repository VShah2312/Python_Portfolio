import random


class Bank:
    def __init__(self) -> None:
        self.acount_number = random.randint(100000, 999999)
        self.holder = input("Enter a name: ").title()
        self.balance = 0.0
        self.account_type = input("Enter a account type: ").title()

    def display(self):
        print(f"\nAccount number: {self.acount_number}")
        print(f"Account holder: {self.holder}")
        print(f"Account balance: {self.balance}")
        print(f"Account type: {self.account_type}\n")

    def withdraw(self):
        amt = float(input("Enter amount to withdraw: "))
        if amt < 0:
            print("Invalid amount")
            return
        if self.balance >= amt:
            self.balance -= amt
            print(f"Updated balance = {self.balance}")
        else:
            print("Insuffciient Balance")

    def deposit(self):
        amt = float(input("Enter amount to deposit = "))
        if amt < 0:
            print("Invalid amount")
            return
        self.balance += amt

    def getBalance(self):
        print(f"Your balance ={self.balance}")


# b1 = Bank()
# b1.display()
# b1.deposit()
# b1.display()
# b1.withdraw()
# b1.display()
# Instead of above way of creating object

accounts: list[Bank] = []

while True:
    # Menu:
    print("\n1. Add account")
    print("2. Display all accounts")
    print("3. Search account")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Exit\n")
    # User choice from input:
    choice = int(input("Enter a choice: "))
    if choice == 1:
        x = Bank()
        accounts.append(x)
    elif choice == 2:
        for obj in accounts:
            obj.display()
    elif choice == 3:
        search_account = int(input("Enter account number to search: "))
        exists = False
        for obj in accounts:
            if obj.acount_number == search_account:
                obj.display()
                exists = True
                break
        if not exists:  # Not False will be True
            print("Account number does not exists.")
    elif choice == 6:
        break
    else:
        print("Invalid Choice")
