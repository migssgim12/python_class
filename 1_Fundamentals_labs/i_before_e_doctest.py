"""
Check that a word follows "I before E except after C".

>>> check("recieve")
recieve doesn't follow the rule


>>> check("receive")
receive does follow the rule

"""
#if i in the said word is before e then True
# if i comes after c then i is after e

def check(word):
    """
    this is checking 'ie' against certain words that are put in the arguments
    also it is taking into consideration the fact that after c it is ei,
    and I do that by evaluating cie in the parameter (word)
    """
    if 'ie' in word:
        print('{} doesn\'t follow the rule'.format(word))
    elif 'cie' in word:
        print('{} doesn\'t follow the rule'.format(word))
    else:
        print('{} does follow the rule'.format(word))
