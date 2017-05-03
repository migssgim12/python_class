"""
Write functions that accept 'dirty' string input, and ouputs a human readable value.
Use a combination of python string methods and regular expressions.

Write, test, and refactor as you go.

>>> scrub_numbers('Be9autiful9 i4s be2tter th4an ug42ly')
'Beautiful is better than ugly.'

>>> gentle_clean('Explicit_is-better_than-implicit')
'Explicit is better than implicit.'

>>> clean_data('  42Simple-is_better_than-compl9ex   ')
'Simple is better than complex.'

>>> some_scrubber('F l a t   i s   b e t t e r   t h a n   n e s t e d . ')
'Flat is better than nested.'

>>> mr_clean('Sparse is better than dense')
' S p a r s e   i s   b e t t e r   t h a n   d e n s e '

>>> ms_clean('Readability counts')
'R9y c4s'

>>> strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly')
'Errors should never pass silently.'

>>> extracto('1S2pe3cia4l ca5ses ar6en't sp7ecial en8ough to b9reak the r0ules.')
45

>>> extracto('2S4pe6cia8l ca0ses ar2en't sp4ecial en6ough to b8reak the r0ules.')
40

>>> extracto('3S6pe9cia2l ca5ses ar8en't sp1ecial en4ough to b7reak the r0ules.')
45
"""

import re

def scrub_numbers(phrase):
    x = re.sub(r'\d','', phrase)
    y = x + '.'
    return y

def gentle_clean(phrase):
    phrase = re.sub(r'[_-]', ' ', phrase)
    result = f'{phrase}.'
    return result

def clean_data(phrase):
    phrase = phrase.strip()
    phrase = re.sub(r'[_-]', ' ', phrase)
    x = re.sub(r'\d', '', phrase)
    result = f'{x}.'
    return result

def some_scrubber(phrase):
    phrase = re.sub(r'(?<=\w)\s(?=\w)', '', phrase)
    phrase = re.sub(r'   ', ' ', phrase)
    phrase = phrase.replace(' . ', '.')
    return phrase

def mr_clean(phrase):
    result = []
    for letter in phrase:
        result = list(result) + [letter, ' ']
    result.insert(0, ' ')
    result = ''.join(result)
    return result

# def ms_clean():



