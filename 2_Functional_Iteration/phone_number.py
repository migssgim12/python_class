# Lab: Fancy Phone Numbers

###### Delivery Method: Prompt Only

##### Goal
""" 
""""""
Write a small app that asks the user for an all-digits phone number, Then 'pretty prints' it out.

##### Instructions

Use the the `input()` builtin function.

Here is an example of the program's expected output:
```
> Please enter an all digits phone number. >> 5035551234

> 503-555-1234



> (503) 555-1234
```

-------------------
#### Documentation

##### [Python Official Docs: input()](https://docs.python.org/3.6/library/functions.html#input)
"""


def gather_input():
    question = input('Please enter an all digits phone number  >> ')

    try:
        question = int(question)

    except ValueError:
        print('Please enter a valid number')
        return gather_input()

    else:
        if not len(str(question)) == 10:
            return gather_input()

    finally:
        x = list(str(question))
        x.insert(0, '(')
        x.insert(4, ')')
        x.insert(8, '-')
        r = ''.join(x)
        return r
