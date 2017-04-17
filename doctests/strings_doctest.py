"""
Return the number of letter occourances in a string.
>>> count_letter('i', 'Antidisestablishmentterianism')
5
>>> count_letter('p', 'Pneumonoultramicroscopicsilicovolcanoconiosis')
2


Return the letter that appears last in the engligh alphabet.
>>> latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
'the latest letter is v.'


Convert input strings to lowercase without any surrounding whitespace.
>>> lower_case("SUPER!")
'super!'
>>> lower_case("        NANNANANANA BATMAN        ")
'nannananana batman'

"""
def count_letter(letter, word):
    count_lets = word.lower().count(letter)
    return count_lets

def latest_letter(word):
    last_lets = max(word)
    return 'the latest letter is {}.'.format(last_lets)

def lower_case(word):
    low_wo_white = word.strip().lower()
    return low_wo_white
