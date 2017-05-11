"""

Account Class - skeleton for code

"""





from bs4 import BeautifulSoup
import requests
import os


class Account:
    def __init__(self, act_type):
        self._balance = 0
        self.interest_rate = 0.01
        self.act_type = act_type


    def get_funds(self):
        return self._balance


    def deposit(self, amount: int):
        self._balance += amount

    def check_withdrawl(self, amount):
        if self._balance < amount:
            return False
        else:
            return True

    def withdrawl(self, amount: int):
        if self.check_withdrawl(amount):
            self._balance -= amount
        else:
            raise ValueError("You don't have enough money!")

    def calc_interest(self):
        self.balance *= 0.01
