"""

#  Leave the line below alone, it is test data.
>>> llamas = [45, 37, 96, 23, 55, 2, 0, 88, 0, 45, 0, 345, 1, 76, 45, 34, 87]

>>> apply_to_all(llamas, 2)
[90, 74, 192, 46, 110, 4, 176, 90, 690, 2, 152, 90, 68, 174]

"""


# Write your code below

def apply_to_all(llamas, n):
    empty_list = []
    for i in llamas:
        if i * n == 0:
            del i
        elif i * n != 0:
            result = i * n
            empty_list.append(result)
    return empty_list