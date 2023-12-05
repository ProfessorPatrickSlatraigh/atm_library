class ATM:
    def __init__(self, bank_system):
        self.bank_system = bank_system
        self.current_account = None

    def insert_card(self, account_id):
        self.current_account = self.bank_system.get_account(account_id)

    def enter_pin(self, pin):
        if not self.bank_system.verify_pin(self.current_account, pin):
            self.current_account = None
            raise ValueError("Invalid PIN")

    def check_balance(self):
        if self.current_account:
            return self.current_account.check_balance()
        raise ValueError("No account selected")

    def deposit(self, amount):
        if self.current_account:
            return self.current_account.deposit(amount)
        raise ValueError("No account selected")

    def withdraw(self, amount):
        if self.current_account:
            return self.current_account.withdraw(amount)
        raise ValueError("No account selected")
