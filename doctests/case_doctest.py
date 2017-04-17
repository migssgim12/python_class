"""
>>> which_case('this_test_text')
'snake_case.'

>>> which_case('this_is_snake_case')
'snake_case.'

>>> which_case('ThisIsCamelCase')
'CamelCase.'

### Advanced ###

>>> snake_to_camel('this_is_snake_case')
'ThisIsSnakeCase'


"""
def which_case(text):
    if '_' in text and text.islower():
        return 'snake_case'
    elif text.isupper():
        return 'CamelCase'
    else:
        return False

