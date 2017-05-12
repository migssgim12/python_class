"""

Functions for the ATM program

"""

from account_class import Account


import sys, time
act = Account  # This is a type annotations


def slowdown_print(type_out):
    for letter in type_out:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.035)


def open_account():
    type_account = ['Checking', 'Savings']
    prompt = input('Enter your name: \n ')
    for index, type in enumerate(type_account, start=1):
        print('Type ', index, 'for ', type)
    while True:
        try:
            act_type = int(input('What type of account would you like?  \n'))
            if act_type == 1:
                act_type = type_account[0]
            elif act_type == 2:
                act_type = type_account[1]
            balan = int(input('What would your initial balance be: \n'))
            account = Account(name=prompt, account_type=act_type, _balance=balan)
            print(f'Thanks {prompt}, you have created a an {act_type} Account, with a {balan} dollar balance. \n')
            break
        except ValueError:
            print('Please enter a valid option. ')
            continue

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
        print('Please choose from the following options: \n')
        for index, option in menu_options.items():
            print(f'<< Press {index} >> to  {option}: ')

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