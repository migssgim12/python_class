"""
>>> letters = [['a', 'b', 'c'], ['d', 'e', 'f', 'g'], ['h', 'i']]

>>> denest(letters)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
"""



# def denest(letters):
#     nesting = letters = letters[0] + letters[1] + letters[2]
#     new_list = list(nesting)
#     return nesting



def denest(letters):
    empty_list = []
    for sublist in letters:
        for item in sublist:
            empty_list.append(item)
    return empty_list


