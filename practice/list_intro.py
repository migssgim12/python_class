"""
>>> a = 'music'
>>> b = [17, 28, 42, 31, 12]

>>> spell_out(a)
m
u
s
i
c

>>> spell_out(b)
17
28
42
31
12

>>> first_and_last(b)
17
12

>>> first_and_last(a)
m
c

"""


def spell_out(a):
    for i in a:
        print(i)

def first_and_last(a):
    print(a[0])
    print(a[-1])