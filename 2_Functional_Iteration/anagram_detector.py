"""

>>> anagram('anagram', 'nag a ram')
True

>>> anagram('Right. One... two... five!', 'Three, sir.')
False

>>> anagram('My ideal time', 'Immediately')
True

"""

# Write your code below.

import string


def clean(word):
    word = word.lower()
    # clean_string = []
    # for char in word:
    #     if char not in string.punctuation and char not in string.whitespace:
    #         clean_string.append(char)
    #
    clean_string = [char for char in word.lower() if char in string.ascii_letters] # list comprehension
    return clean_string


def anagram(a, b):
    a, b = clean(a), clean(b) #parallel assignment
    result = True if sorted(b) == sorted(a) else False  # Ternary operation
    return result
