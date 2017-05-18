"""
Michael J Poehner

PhPonebook Solution

"""


import chalk


phonebook = dict()


def leave():
    print('Ok you decided to leave. Get out of here then. You are a loser anywayy')
    quit()


def add_person():
    add_in = input('Please enter a name >>')
    phone_number = input('Please enter a phone number >>')
    chalk.blue(f'Thanks. You have added, {add_in} who has a phone number of:  {phone_number}')
    phonebook[add_in] = {'Name': add_in, 'Phone': phone_number}


def list_people():
    if len(phonebook) == 0:
        print('You do not have anyone in your phone-book! \n')
    else:
        print('You have these people in your phone book: \n ')
        for nick, entry in phonebook.items():
            for key, value in entry.items():
                print(key, value, sep=': ')
            print('*' * 9)


def retrieve():
    one_person = input('What is the name you want to look up? ')
    if one_person in phonebook[one_person]['Name']:
        print(phonebook[one_person]['Name'], 'has a phone number of: ', phonebook[one_person]['Phone'])
        cont = input('Would you like to continue with this fabulous phone-book?  ')
        if cont == 'yes':
            phone_book()
        else:
            print('Ok see ya later')
            quit()
    else:
        print(f'{one_person} is not in the phonebook')


def phone_book():
    prompt = '''What would you like to do: 
              Add a phone number (enter 'add')
              Remove a phone number (enter 'remove')
              Get the phone-book list (enter 'list')
              Retrieve a contact in a list (enter 'get')
              Quit the application (enter 'quit')
              >>> '''

    options = {'quit': leave,
               'list': list_people,
               'add': add_person,
               'get': retrieve,
               'remove': remove_contact,
               'update': update_contact
               }

    while True:
        choice = input(prompt).lower()
        try:
            options[choice]()
        except KeyError:
            print('invalid choice')
            continue


def remove_contact():
    list_people()
    to_remove = input('What would you like to remove? \n  >>')
    try:
        del phonebook[to_remove]
    except KeyError:
        print(f'{to_remove} is not in the phonebook')


def update_contact():
    list_people()
    one_name = input('Who do you want to update?')

    try:
        exists = one_name in phonebook[one_name]['Name']
    except KeyError:
        print(f'{one_name} is not in the phonebook')
        return update_contact()

    if exists:
        change_name = input('What do you want to change, name or phone? ')
        if change_name == 'name':
            change_name2 = input('What do you want the name to change to? ')
            phonebook[one_name]['Name'] = change_name2
        elif change_name == 'phone':
            change_name3 = input('Phone number? ')
            phonebook[one_name]['Phone'] = change_name3
        else:
            print('what')

    return one_name


if __name__ == '__main__':
    phone_book()