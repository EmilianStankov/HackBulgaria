import bank
import unittest


class BankTest(unittest.TestCase):

    def test_get_balance(self):
        self.assertEqual(bank.balance, bank.get_balance())

    def test_deposit_money(self):
        bank.deposit_money(100)
        self.assertEqual(100, bank.get_balance())

    def test_withdraw_money(self):
        bank.balance = 100
        bank.withdraw_money(75)
        self.assertEqual(25, bank.get_balance())

    def test_deposit_negative_amount_of_money(self):
        self.assertEqual(False, bank.deposit_money(-100))

    def test_withdraw_negative_amount_of_money(self):
        self.assertEqual(False, bank.withdraw_money(-100))

if __name__ == '__main__':
    unittest.main()
