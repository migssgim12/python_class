"""

>>> exclude_em([56, 57, 58, 59, 60], 57)
[56, 59, 60]

>>> exclude_em([43, 67, 456, 23, 878, 5, 65, 34], 456)
[43, 67, 878, 5, 65, 34]

>>> exclude_em([43, 67, 456, 23, 878, 5, 65, 34])
[456, 23, 878, 5, 65, 34]

>>> double([43, 67, 456, 23, 878, 5, 65, 34], [2, 1, 1, 2, 2, 0, 0, 0])
[86, 67, 456, 46, 1756, -1, -1, -1]

>>> punch_in([43, 67, 456, 23, 878, 5, 65, 34], [2, 1, 1, 2, 2, 0, 0, 0], 2)
[43, 67, 2, 1, 1, 2, 2, 0, 0, 0, 456, 23, 878, 5, 65, 34]

"""

def exclude_em(listy, inty=None):
    if not inty:
        del listy[0:2]
        result = listy
    elif inty in listy:
        position = listy.index(inty)
        del listy[position:position + 2]
        result = listy
    else:
        pass

    return result

def double(a,b):
    result = []
    for a, b in zip(a, b):
        if a == 0 or b == 0:
            c = -1
            result.append(c)
        else:
            result.append(a * b)
    return result

def punch_in(list1, list2, inty):
    for i in list1:
        list1.insert([i], list2)
        result = list1
    return list