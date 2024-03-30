import random


class Bank:
    def __init__(self) -> None:
        self.acount_number = random.randint(100000, 999999)
        self.holder = input("Enter a name: ").title()
        self.balance = 0.0
        self.account_type = input("Enter a account type: ").title()

    def display(self) -> None:
        print(f"\nAccount number: {self.acount_number}")
        print(f"Account holder: {self.holder}")
        print(f"Account balance: {self.balance}")
        print(f"Account type: {self.account_type}\n")

    def withdraw(self, amt: float) -> None:
        if amt < 0:
            print("Invalid amount")
            # return by itself to break out of function/method.
            return
        if self.balance >= amt:
            self.balance -= amt
            print(f"Updated balance after withdraw = {self.balance}")
        else:
            print("Insuffciient Balance")

    def deposit(self, amt: float) -> None:
        if amt < 0:
            print("Invalid amount")
            return
        self.balance += amt
        print(f"Updated balance after deposit = {self.balance}")

    def getBalance(self):
        print(f"Your balance ={self.balance}")


# Accounts is list of objects from Bank Class
accounts: list[Bank] = []

while True:
    # Menu:
    print("\n1. Add account")
    print("2. Display all accounts")
    print("3. Search account")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Transfer")
    print("7. Exit\n")

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
    elif choice == 4:
        search_account = int(input("Enter a account number to deposit: "))
        exists = False
        for obj in accounts:
            if obj.acount_number == search_account:
                deposit_amt = float(input("Enter amount to deposit: "))
                obj.deposit(deposit_amt)
                obj.display()
                exists = True
                break
        if not exists:
            print("Account number does not exists.")
    elif choice == 5:
        search_account = int(input("Enter a account number to withdraw from: "))
        exists = False
        for obj in accounts:
            if obj.acount_number == search_account:
                withdraw_amt = float(input("Enter amount to withdraw: "))
                obj.withdraw(withdraw_amt)
                obj.display()
                exists = True
                break
        if not exists:
            print("Account number does not exists.")
    elif choice == 6:
        withdraw_account = int(input("Enter a account number to withdraw from: "))
        deposit_account = int(input("Enter a account number to deposit in: "))
        exists_w = False
        exists_d = False
        for obj in accounts:
            if obj.acount_number == withdraw_account:
                transfer_withdraw = obj
                exists_w = True
                break
        if not exists_w:
            print("Withdraw account number does not exists.")
        for obj in accounts:
            if obj.acount_number == deposit_account:
                transfer_deposit = obj
                exists_d = True
                break
        if not exists_d:
            print("Deposit account number does not exists.")

        if exists_w and exists_d:
            amount = float(input("Enter amount to transfer: "))
            transfer_withdraw.withdraw(amount)
            transfer_deposit.deposit(amount)
            print("Transfer Sucessful.")
    elif choice == 7:
        break
    else:
        print("Invalid Choice")
