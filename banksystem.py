class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.account_pins = {}

    def add_account(self, account, pin):
        self.accounts[account.account_id] = account
        self.account_pins[account.account_id] = pin

    def get_account(self, account_id):
        return self.accounts.get(account_id)

    def verify_pin(self, account, pin):
        return self.account_pins.get(account.account_id) == pin
