"""
Rain data analysis

"""

from bs4 import BeautifulSoup
import requests
import os

BASE_DIR = '/home/migs/Documents/python_class/3_AppliedPython/rain'

def max_day(data: dict) -> None:
    maxrainday =max(data.items(), key=lambda t: t[1][0])
    print(f'It rained {maxrainday[1][0]} plops on {maxrainday[0]}')


def clean_data(datus: list) -> list:
    splittered = datus[11:]
    splittered = [line.split() for line in splittered]
    splittered = [data for data in splittered if data != []]
    """ This is taking the empty lists and eliminating them """
    taking_apart = {rainday[0]: (int(rainday[1]), rainday[2:]) for rainday in splittered if '-' not in rainday[1:]}
    """ First the dictionary comprehension is creating a key that is the date. Then, It is taking the first element(which is the sum of the hourly data.) Then I am taking the first element in the list and isolating it with the rest of the items with a tuple. I am ignoring the '-'. 
    """

    return taking_apart


def file_handler(path: str) -> str:
    with open(path, 'r')as f:
        text = f.read()
        return text


def parser():
    path = os.path.join(BASE_DIR, 'sample.rain')
    file_handler(path)
    data = file_handler(path)
    data = data.split('\n')
    great_data = clean_data(data)
    max_day(great_data)


parser()
