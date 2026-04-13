class BankAccount():
    """Класс банковский счет"""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Пополнение счета"""
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Снятие со счета"""
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Not enoung money"

    def get_balance(self):
        return self.balance
