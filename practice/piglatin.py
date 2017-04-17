"""
Pig latin

Program that asks for a single English word and translates to Pig latin
If the first letter is a constant. move it to the end
Add "ay" to the end of that.
If the first letter is a vowel, just ad "yay" to the end.

"""

# First ask for a word

def pig_word(word):
    ay ='ay'
    word2 = word[1:]
    pig_latin = word2 + ay
    pig_latin2 = word + ay
    if word not in ['a','e','i','o','u']:
        result = pig_latin
    else:
        result = pig_latin2

    print(result)
    return result

def gather_input():
    word = input('Enter a sentence  >>')
    pig_word(word)



gather_input()






# Seeing if the first letter of the word is a consonant
