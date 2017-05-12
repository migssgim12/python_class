import unittest
from account_class import Account


class TestAccountCreation(unittest.TestCase):
    def setUp(self):
        self.test_caccount = Account(name='Jorge', _balance=270, account_type='checking')
        self.test_saccount = Account(name='George', _balance=10454, account_type='savings')

    def test_initial_checking_account_open(self):
        self.assertNotEqual(self.test_caccount._balance, 210)
        self.assertEqual(self.test_caccount.account_type, 'checking')

    def test_initial_savings_account_open(self):
        self.assertEqual(self.test_saccount._balance, 10454)
        self.assertEqual(self.test_saccount.account_type, 'savings')

    def test_account_creation_from_csv_string(self):
        record = '5902692944186857,151.5,checking'
        test_account = Account.from_csv_string(record)
        self.assertEqual(test_account._balance, 151.50)
        self.assertEqual(test_account.account_type, 'checking')

class TestAccountOperations(TestAccountCreation):

    def test_get_balance(self):
        test_account = Account(name='Jorge',_balance=500, account_type='checking')
        self.assertEqual(test_account.get_funds(), 500)
        test_account.withdrawl(250)
        self.assertEqual(test_account.get_funds(), 250)

    def test_valid_withdraw_in_good_standing(self):
        self.assertEqual(self.test_saccount.withdrawl(100), 10354)

    def test_overdraw_error(self):
        with self.assertRaises(ValueError):
            self.test_caccount.withdrawl(999999999)

    def test_deposit(self):
        self.assertEqual(self.test_caccount.deposit(100), 370)

    def test_simple_interest(self):
        pass

    def test_check_withdraw_bool(self):
        self.assertFalse(self.test_caccount.check_withdrawl(999999999))

    def test_get_standing_bool(self):
        self.assertFalse(self.test_caccount.get_standing())
        self.assertTrue(self.test_saccount.get_standing())


class TestATMInterface(TestAccountCreation):
    def test_checkbalance(self):
        test_account = Account(name='Jorge', account_type='checking')
        self.assertEqual(test_account.get_funds(), 500)
        test_account.withdrawl(250)
        self.assertEqual(test_account.get_funds(), 250)
