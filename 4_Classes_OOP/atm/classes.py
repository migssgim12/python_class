"""

Account Class

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
        pass

    def deposit(self, amount):
        self._balance += amount

    def check_withdrawl(self, amount):
        if self._balance < amount:
            return False
        else:
            return False

    def calc_interest(self):
        pass

x = Account('emu')
x.deposit(233)
