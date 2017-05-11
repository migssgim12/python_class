"""

Functions for the ATM program

"""

from classes import Account

import sys, time
act = Account

def slowdown_print(type_out):
    for letter in type_out:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.035)


def open_account():
    prompt = input('Enter your name:  ')
    account = Account(prompt)
    print(f'Thanks {prompt}, you have created an account. \n')
    type_out = ('Now choose from the following options: \n')
    slowdown_print(type_out)
    return account


def check_balance(account: act):
        print(f'You have {account.get_funds()} dollars.')



def deposit(account: act):
    amount = int(input('How much are you going to deposit?  '))
    account.deposit(amount)
    print(f'Now you have {account.get_funds()} dollars.')
    


def withdrawl(account: act):
    amount = int(input('How much do you want?  '))
    account.withdrawl(amount)
    print(f'Now you have {account.get_funds()} dollars.')
    
    
def menu():

    print('Welcome to the Machine. What would you like to do?  ')
    prompt = "<<<------------------------------>>> \n"
    options = ['Open an Account', 'Check your Balance', 'Make a Deposit', 'Withdraw Funds']

    menu_options = {index: option for index, option in enumerate(options, start=1)}

    while True:
        for index, option in menu_options.items():
            print(f'<<Press {index} >> to  {option}')

        try:
            choice = int(input(prompt).lower())
            if choice == 1:
                account = open_account()
            elif choice == 2:
                check_balance(account)
            elif choice == 3:
                deposit(account)
            elif choice == 4:
                withdrawl(account)

        except ValueError:
            print("Invalid Choice! It's not that hard. 1, 2, 3, or 4. \nTry again:  ")
            continue

menu()