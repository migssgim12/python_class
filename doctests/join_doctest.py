"""
Write functions that convert two input args into kebab-case string output.

>>> link('Chuck', 'Norris')
'Chuck-Norris'

>>> link("hello", 1)
'hello-1'

>>> link(40, 2)
'40-2'
"""

def link(first, second):
    joins = [str(first), str(second)]
    result = '-'.join(joins)
    return result

# link('chuck','noris')
