class Account:
    def __init__(self, account_id, balance=0):
        self.account_id = account_id
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return amount
