import random


answer = True
no_responses = ('no', 'nah', 'nope', 'no', '',)
yes_responses = ('yes', 'ya', 'yup')


def play_again():
    again = input('Do you want to play again?  >> ')
    if again in yes_responses:
        print('ok lets go!')
    else:
        print('thanks for playing')
        return quit()
y

def greeting():
    greeting = input('Do you want to play 8 ball?' )
    if greeting in yes_responses:
        print('Ok, lets boogy!')
    else:
        print('Ok fine then. Its your loss. ')
        return quit()



while answer:
    greeting()
    answers = random.randint(1, 10)
    gather_input2 = input(' What is your question? >> ')


    if answers == 0:
        print('Only time will tell....')
    elif answers == 1:
        print('It is certain. ')
    elif answers == 2:
        print('It is decidely so. ')
    elif answers == 3:
        print('Without a doubt. ')
    elif answers == 4:
        print('Yes definitely. ')
    elif answers == 5:
        print('Maybe if you changed your attitude! ')
    elif answers == 6:
        print('You are a loser, so no.')

    play_again()

print('thanks for playing')