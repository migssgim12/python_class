
"""
Write a simple program that, when run, prompts the user for their name and age, then prints a greeting and a message about how old they will be a year from now.

1. Open Atom
1. Create a new file and save it as `greeting.py`
1. Implement the program, ideally without peeking at the solution
"""
def greet():
    name = input('What is your name?  >>')
    age = int(input('What is your age?  >>'))
    age = age + 1
    print('Hi {}, You will be {} in one year'.format(name, age))

greet()
