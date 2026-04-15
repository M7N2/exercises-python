# Test bank_account.py
import unittest
from bank_account import BankAccount

class BankTestCase(unittest.TestCase):
    """Test 'bank_account.py' """

    def setUp(self):
        self.new_owner = BankAccount('ronald reigan', 1000)

    def test_deposit(self):
        """Checking balance replenishment"""
        self.new_owner.deposit(5000)
        self.assertEqual(self.new_owner.balance, 6000)

    def test_withdraw(self):
        """Checking withdrawals"""
        self.new_owner.withdraw(1000)
        self.assertEqual(self.new_owner.balance, 0)

    def test_withdraw_negative(self):
        """Checking withdrawals with insufficient balance"""
        initial_balance = self.new_owner.balance
        result = self.new_owner.withdraw(1500)
        self.assertEqual(self.new_owner.balance, initial_balance)
        self.assertEqual(result, "Not enoung money")

    def test_get_balance(self):
        """Checking balance"""
        result = self.new_owner.get_balance()
        self.assertEqual(result, 1000)            

if __name__ == '__main__':
    unittest.main()
