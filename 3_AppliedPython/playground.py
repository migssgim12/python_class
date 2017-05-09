
import os


BOOKS = '/home/migs/Documents/python_class/3_AppliedPython/Ari/books'

def get_data(path):
    with open(path, 'r') as file:
        text = file.read()
        return text

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
        print(menu)
        text = get_data(fullpath)
        # print(menu)
        print(text)


show_menu()
