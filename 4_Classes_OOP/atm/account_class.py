"""

Account Class - skeleton for code

"""


from bs4 import BeautifulSoup
import requests
import os


class Account:
    def __init__(self, name, _balance, account_type):
        self.name = name
        self._balance = _balance
        self.interest_rate = 0.01
        self.account_type = account_type

    @classmethod
    def from_csv_string(cls, csv_string):
        name, _balance, account_type = csv_string.split(',')
        _balance = float(_balance)
        act = cls(name, _balance, account_type)
        return act

    def get_funds(self):
        return self._balance

    def get_standing(self):
        if self._balance >= 1000:
            return True
        else:
            return False

    def deposit(self, amount: int):
        self._balance += amount
        return self._balance

    def check_withdrawl(self, amount: int):
        if self._balance < amount:
            return False
        else:
            return True

    def withdrawl(self, amount: int):
        if self.check_withdrawl(amount):
            self._balance -= amount
        else:
            raise ValueError("You don't have enough money!")
        return self._balance


    def calc_interest(self):
        self._balance *= 0.01
