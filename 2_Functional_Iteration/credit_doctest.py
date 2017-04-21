"""

>>> validate([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5])
Valid!

>>> validate([6, 5, 1, 6, 4, 3, 7, 5, 1, 6, 4, 9, 3, 8, 5, 4])
Invalid!

"""


def validate(account_number):
    check_digit = account_number.pop()  # slice last digit off
    reversing = account_number[::-1]  # reverse

    for i in range(0, len(reversing), 2):
        reversing[i] = reversing[i] * 2

        if reversing[i] > 9:
            reversing[i] = reversing[i] - 9

    added_up = sum(reversing)
    second_digit = int(str(added_up)[1])

    if second_digit == check_digit:
        print('Valid!')
    else:
        print('Invalid!')




