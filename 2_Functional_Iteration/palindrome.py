


def palindrome(word):

    rev =reversed(word)

    if word == word [::-1]:
        return True
    else:
        return False

palindrome('anything')