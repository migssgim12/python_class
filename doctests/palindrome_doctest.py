"""
Write a function that returns True if the input is a palindrome, or False, if it is not.

>>> palindrome('hannah')
True

>>> palindrome('racecar')
True

>>> palindrome('a man, a plan, a canal, Panama')
True

>>> palindrome("1 pound coconut.")
False

>>> palindrome(1234321)
True

"""
def palindrome(noun):
    # First take the data, eliminate commas, spaces, and make everything lowercase so I can
    # use the function to evaluate cleaned version
    stringified = str(noun).replace(',', '').replace(' ', '').lower()
    # Now I am going to rev_noun is equal to what it is backwards
    rev_noun = stringified[::-1]
    print(rev_noun)
    if rev_noun == stringified:
        result = True
    else:
        result = False
    return result
