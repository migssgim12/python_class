"""

>>> shrink('1235')
2

>>> shrink('13')
4

>>> shrink('1123581321')
9

"""

def shrink(weed):
    pound = sum(int(ounce) for ounce in list(weed))
    if len(str(pound)) >= 2:
        return shrink(str(pound))
    else:
        return pound
