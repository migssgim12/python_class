shopping_list = []


def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
Enter 'REMOVE' to delete an item from your list
""")


def add_to_list(item):
    shopping_list.append(new_item)
    print("Added! List has {} items.".format(len(shopping_list)))


def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)

def remove_from_list():
    show_list()
    what_to_remove = input('What would you like to remove? \n >')
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()

show_help()

while True:
    new_item = input("> ")

    if new_item.upper() == 'DONE':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
        continue

    add_to_list(new_item)

show_list()