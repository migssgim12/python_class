"""
Michael J Poehner

Voting Booth Program

"""

candidates_voting = {}
candidates = ['Carl Van Loon', 'Bradley Cooper', 'Linda Lovelace', 'Hulk Holgan', 'Jenny McCarthy' ]
def voting_booth():
    print('Welcome to the voting booth! Please vote or hide your head in the sand because you don\'t matter anyway!')
    for index, element in enumerate(candidates, start=1):
        print('Press', index, 'for', element)

def votes():
    candidates_voting = {el: 0 for el in candidates}





