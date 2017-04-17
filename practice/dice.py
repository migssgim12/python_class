"""
This is a program that asks the user
for the number of dice they want to roll as well as the number of sides per die.
We will use the random Module
"""

import random


def roll(dice, sides):
    for i in range(dice): #
        roll = random.randint(1, sides)
        print(roll)


def gather_input():
    dice = int(input('How many dice do you want?  >>'))
    sides = int(input('How many sides?  >>'))
    roll(dice, sides)

gather_input()
