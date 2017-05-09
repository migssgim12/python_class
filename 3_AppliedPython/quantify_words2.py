path = '/home/migs/Documents/PythonFullStack/1_Python/3_Applied_Python/labs/ari/books/jack_and_jill.txt'

def get_data(path):
    with open(path, 'r') as file:
        text = file.read()
        return text





def get_data2(path):
    num_words = 0
    occurences = 0
    with open(path, 'r') as file:
        for line in file:
            words = line.split()
            num_words += len(words)

        print(num_words)

get_data2(path)
