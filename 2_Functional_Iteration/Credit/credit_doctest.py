"""

>>> validate([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5])
Valid!

>>> validate([6, 5, 1, 6, 4, 3, 7, 5, 1, 6, 4, 9, 3, 8, 5, 4])
Invalid!

"""


def validate(account_number):
    check_digit = account_number.pop()  # slice last digit off
    reversing = account_number[::-1]     # reverse

    result = list()
    for i in range(0, len(reversing), 1):
        item = reversing[i]
        if i % 2 == 0:
            x = item * 2
        else:
            x = item

        if x > 9:
            x -= 9

        result.append(x)

    added_up = sum(result)
    second_digit = int(str(added_up)[1])

    if second_digit == check_digit:
        print('Valid!')
    else:
        print('Invalid!')


