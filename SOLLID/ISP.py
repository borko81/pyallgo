"""
A client should not be forced to implement an interface that id does not use
"""


class BankAcc:
    def __init__(self, account: str, balance: float):
        self.account = account
        self.balance = balance

    def balance(self):
        return self.account, self.balance


class Deposit:
    def deposit(self, amount: float, account: BankAcc):
        current = account.balance
        new_amount = current + amount
        account.balance = new_amount


b = BankAcc('Borko', 100)
d = Deposit().deposit(100, b)
print(b.balance)

