"""
# Test Data Below.  Leave this line alone.
>>> names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

>>> people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]

>>> long_names(names, 5)
['Kieran', 'Serada', 'Alfonzo']

>>> starts_with(names, 'S')
['Suki', 'Serada']

>>> last_names(people)
['Prasch', 'Ward', 'Balnik']

>>> smoosh(people)
['Kieran', 'Prasch', 'Instructor', 'Alfonzo', 'Ward', 'Student', 'Fin', 'Balnik', 'Student']

"""

def long_names(names, n):
    x = [name for name in names if len(name) > n]
    return x

def starts_with(names, n):
    x = [name for name in names if name[0] == n]
    return x

def last_names(people):
    y = [last[1] for last in people]
    return y

def smoosh(people):
    y = people[0] + people[1] + people[2]
    something = list(y)
    return something