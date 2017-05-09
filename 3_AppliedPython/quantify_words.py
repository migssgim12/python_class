
import string
import re


def get_data(path: str):
    with open(path, 'r' ) as file:
        text = file.read()
        return text


def cleaning(phrase: str) -> str:
    """
    Taking the white space out
    """
    pattern = re.compile(r'['+string.punctuation+']')
    small = phrase.lower()
    cleaned = pattern.sub(' ', small) # Taking the , and .

    return cleaned


def display_results(count_word: dict, qty=10) -> None:
    for k, v in sorted(count_word.items(), key=lambda t: t[1], reverse=True)[:qty]:
        print(k, v)



def quantify_words(path: str):

    phrase = get_data(path)  # Assigning a variable to the function so that we can capture the return value later on
    cleanstring = cleaning(phrase)  # Assigning phrase to a new variable
    splitter = cleanstring.split()  # this takes the whitespace out

    count_word = dict()           # Initialize empty dictionary to put values in
    for word in splitter:
        try:
            count_word[word] += 1 # This increments the amount of instances of a certain word
        except KeyError:
            count_word[word] = 1

    display_results(count_word)




quantify_words('/home/migs/Documents/PythonFullStack/1_Python/3_Applied_Python/labs/ari/books/jack_and_jill.txt')


