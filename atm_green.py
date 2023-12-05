class ATM:
    def __init__(self, account):
        self.account = account

    def check_balance(self):
        if not self.account:
            raise ValueError("No account selected")
        return self.account.balance  # Assuming 'balance' is an attribute of Account
