import random


class Bank:

    def __init__(self) -> None:
        self.account_holder_name: str = input("Enter account holder name: ").title()
        self.account_number: int = random.randint(100000, 999999)
        self.balance: float = 100
        self.account_type: str = input(
            "Enter account type (Checking/Savings): "
        ).title()

    def displayAllInfo(self) -> None:
        print(f"\nAccount holder name= {self.account_holder_name}")
        print(f"Account Number= {self.account_number}")
        print(f"Account Type= {self.account_type}")
        print(f"Balance= {self.balance}")

    def deposit(self, amount: float) -> float:
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float | str:
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        return None

    def getBalance(self) -> float:
        return self.balance


if __name__ == "__main__":
    # Creating a bank account object:
    account1 = Bank()

    # Display all information about the bank account:
    account1.displayAllInfo()

    # Deposit 1000 into the account:
    after_deposit = account1.deposit(1000.00)
    print("After Deposit, balance= ", after_deposit)

    # Withdraw 2000 from the account:
    after_withdraw = account1.withdraw(2000.00)
    if after_withdraw != None:
        print("After Deposit, balance= ", after_deposit)
    else:
        print("Insufficient Balance")

    # Get the current balance in the account:
    current_balance = account1.getBalance()
    print("Current Balance: ", current_balance)
