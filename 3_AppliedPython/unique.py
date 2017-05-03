"""
>>> things = ['flowers', 'puddle', 'mouse', 'keyboard', 'bread', 'house', 'mouse']
>>> living_things = ['mouse', 'flowers', 'trees', 'shrubs', 'mouse']
>>> computer_parts = ['mouse', 'keyboard']


>>> unique(things)
6

>>> unique(living_things)
4

>>> unique(computer_parts)
2

>>> unique(things, living_things)
8

>>> common(things, living_things)
2

>>> common(things, living_things, computer_parts)
1

>>> common(living_things, computer_parts)
1

"""



def unique(items, *args):
    x = set(items)
    y = set(*args)
    x.update(y)
    print(len(x))

def common(items, *args):
    x = set(items)
    y = set(*args)
    a = y.intersection(x)
    print(len(a))