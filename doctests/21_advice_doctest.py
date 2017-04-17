"""
Make a function that advises a player on the best next move in a round of blackjack.
For now, just use 15 as a Hit/Stay Threshold.  Feel free to add testable features.

>>> advise_player(10, 5)
15 Hit.

>>> advise_player('Q', 5)
15 Hit.

>>> advise_player('A', 'K')
21 Blackjack!

>>> advise_player('J', 'K')
20 Stay.

"""


def advise_player(card1, card2):
    face_cards = ('K', 'Q', 'J')  #Defining variables -
    ace = 'A'

    try:
        card1 = int(card1)
    except ValueError:
        if card1 in face_cards:
            card1 = 10
        elif card1 in ace:
            card1 = 11

    try:
        card2 = int(card2)
    except ValueError:
        if card2 in face_cards:
            card2 = 10
        elif card2 in ace:
            card2 = 11

    hand = card1 + card2

    if hand == 15:
        print('15 Hit.')
    elif hand == 21:
        print('21 Blackjack!')
    elif hand == 20:
        print('20 Stay.')





