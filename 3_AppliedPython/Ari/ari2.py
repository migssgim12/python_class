"""

ARI program

Michael Poehner

"""

import os

BOOKS = '/home/migs/Documents/python_class/3_AppliedPython/Ari/books'


def get_data(path):
    with open(path, 'r') as file:
        text = file.read()
        return text


def strong_scrubber(raw: str) -> str:
    pass


def get_chars_words_lines(text: str):
    n_words = len(text.split())
    n_chars = len(list(text))
    sentences = text.count('.')
    return n_words, n_chars, sentences


def calc_ari(words: int, chars: int, sents: int) -> int:
    pass


def show_menu():
    """
    :return: 
    """
    paths = os.listdir(BOOKS)
    paths = [path for path in paths if '.txt' in path]
    menu = {i: text for i, text in enumerate(paths, start=1)}
    menu2 = {}

    print('=======<<>><<>><<>>=======')
    for number, path in menu.items():
        print(f'{number}) {path}')

    while True:
        prompt = input('What book would you like to analyze?')
        try:
            prompt = int(prompt)

        except ValueError:
            print('')
            quit()

        choice = menu[prompt]
        fullpath = os.path.join(BOOKS, choice)
        text = get_data(fullpath)

        return text


def do_it():
    raw = show_menu()
    # text = strong_scrubber(raw)
    n_words, n_chars, sentences = get_chars_words_lines(text)
    # score = calc_ari(n_words, n_chars, sentences)
    x = get_chars_words_lines(text)
    print(score)

show_menu()