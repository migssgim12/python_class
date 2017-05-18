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


def get_chars_words_lines(path: str):

    text = get_data(path)

    n_words = len(text.split())
    n_chars = len(list(text))
    sentences = text.count('.')
    return n_words, n_chars, sentences

a, b, c = get_chars_words_lines('')


def show_menu():
    """
    :return: 
    """
    paths = os.listdir(BOOKS)
    paths = [path for path in paths if '.txt' in path]
    menu = {i: text for i, text in enumerate(paths, start=1)}
    menu2 ={}

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
        text2 = get_chars_words_lines(fullpath)
        # print(text)
        print(text2)


show_menu()


