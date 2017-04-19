"""



>>> together('knights', 'camalot')
k c
n a
i m
g a
h l
t o
s t

>>> together('books', 'fantasy')
b f
o a
o n
k t
s a
  s
  y
"""


# def together(a, b):
#     for a,b in zip(a, b):
#         print(a, b)


# def together(a, b):
#     for index in range(0, len(a)):
#         print(a[index], b[index])

from itertools import zip_longest

# def together(a, b):
#     counter = 0
#     while counter < len(b):
#         print(a[counter], b[counter])
#         counter += 1

def together(a, b):
    for a, b in zip_longest(a, b, fillvalue=' '):
        print(a, b)

