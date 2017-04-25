"""

>>> fizz_buzz(15)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

REMEMBER: Use Encapsulation! D.R.Y.
>>> joined_buzz(15)
'1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz'

"""


def fizz_buzz(n):
    empty_list = []
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            empty_list.append('FizzBuzz')
        elif i % 3 == 0:
            empty_list.append('Fizz')
        elif i % 5 == 0:
            empty_list.append('Buzz')
        else:
            empty_list.append(str(i))

    return empty_list


def joined_buzz(n):
    empty_list = []
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            empty_list.append('FizzBuzz')
        elif i % 3 == 0:
            empty_list.append('Fizz')
        elif i % 5 == 0:
            empty_list.append('Buzz')
        else:
            empty_list.append(str(i))
    return ' '.join(empty_list)
