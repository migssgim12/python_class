"""I'm the module level Docstring... Fill Me Out!"""

import random


# Uncomment the import above and write your code below.


no_responses = ('no', 'nah', 'nope', 'no', '',)
yes_responses = ('yes', 'ya', 'yup')

def greeting():
    greet = input('Hello, would you like to play the number guessing game?  \n >>')
    if greet in yes_responses:
        print('Ok lets go!')
    else:
        print('Ok no problem, see you later')
        return quit()

answer = True
while answer:
    greeting()
    answers = random.randint(1, 2_000_000_000)
    gather_input = input('What is a number between one and 2 billion? \n  >>')
    if gather_input == answers:
        print('Great Job! ')
        break
    else:
        print('Oh you got a long way to go! ')

    if gather_input


hi_number = 2_000_000_000
low_number = 0




print('Thanks for playing')

