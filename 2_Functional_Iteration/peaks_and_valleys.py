"""

>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

>>> peaks(data)
[6, 14]

>>> valleys(data)
[9, 17]

>>> peaks_and_valleys(data)
[6, 9, 14, 17]

>>> points_of_interest = peaks_and_valleys(data)

>>> chop(data, points_of_interest)
[[1, 2, 3, 4, 5, 6, 7], [6, 5, 4], [5, 6, 7, 8, 9], [8, 7, 6], [7, 8, 9]]

"""


def peaks(data):
    peakys = []
    for index, num in enumerate(data):
        if index == 0 or index == (len(data) - 1):
            continue
        middle = data[index]
        next_one = data[index + 1]
        previous_one = data[index - 1]
        if middle > next_one and middle > previous_one:
            peakys.append(index)
    return peakys


def valleys(data):
    peakys = []
    for index, num in enumerate(data):
        if index == 0 or index == (len(data) - 1):
            continue
        middle = data[index]
        next_one = data[index + 1]
        previous_one = data[index - 1]
        if middle < next_one and middle < previous_one:
            peakys.append(index)
    return peakys

def peaks_and_valleys(data):
    p_av = peaks(data) + valleys(data)
    return sorted(p_av)

def points_of_interest():
    return peaks_and_valleys(data)

def chop(data, points_of_interest)
    for index,



