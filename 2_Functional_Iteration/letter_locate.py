"""

>>> locate('l', 'hello')
[2, 3]

>>> locate('b', 'bannanas')
[0]

>>> locate('i', 'mississippi')
[1, 4, 7, 10]
"""

def locate(letter, word):
    empty_list = []
    for index, char in enumerate(word):
        if char == letter:
            empty_list.append(index)
    return empty_list



# y = [index for index, char in enumerate(word) if char == target]

