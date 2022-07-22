"""
The class should have only one responsibility and one reason to change
that mean a class does not perform multiple jobs
"""


class Account:
    def __init__(self, account_no: str):
        self.account_no = account_no

    def get_account_number(self):
        return self.account_no


class AccountDB:
    def __init__(self, account_no: str):
        self.account = account_no

    def save(self):
        pass


a = Account('A1234')
print(a.get_account_number())
db = AccountDB(a.get_account_number())
db.save()
