class BankAccount():
    """Class Bank account"""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Account replenishment"""
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Withdrawal from account"""
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Not enoung money"

    def get_balance(self):
        return self.balance
