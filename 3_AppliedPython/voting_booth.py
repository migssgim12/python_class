"""
Michael J Poehner

Voting Booth Program

"""
candidates_voting = {}
candidates = ['Carl Van Loon', 'Bradley Cooper', 'Linda Lovelace', 'Hulk Holgan', 'Jenny McCarthy' ]


def voting_booth():
    print('Welcome to the voting booth! Please vote or hide your head in the sand!')
    candidates_voting = {el: 0 for el in candidates}
    candidate_choices = {i: cand for i, cand in enumerate(candidates_voting, start=1)}

    while True:
        list_of_candidates()
        prompt = input('>>  ')
        try:
            prompt = int(prompt)
            choice = candidate_choices[prompt]
            candidates_voting[choice] += 1
            al_lignment(candidates_voting, 20, 7)
            # for key in candidates_voting:
            #     print(key, candidates_voting.get(key), sep=' has ')

            continue
        except ValueError:
            if prompt == 'done':
                al_lignment(candidates_voting, 20, 7)
                break
                # for key in candidates_voting:
                #     print(key, candidates_voting.get(key), sep=' has ')
                # break
            elif prompt =='list':
                print('These are the tallies so far: ')
                al_lignment(candidates_voting, 20, 7)
                # for key in candidates_voting:
                #     print(key, candidates_voting.get(key), sep=' has ')
                continue
            print('Please enter a valid number')
            continue


def list_of_candidates():
    for index, element in enumerate(candidates, start=1):
        print('Press', index, 'for', element)
    print("Enter 'done' to quit, or 'list' to list the tallies")


def al_lignment(items_dict, leftWidth, rightWidth):
    print('Vote Tally:'.center(leftWidth + rightWidth, '-'))
    for k, v in items_dict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
    return items_dict


def tally_list():
    for key in candidates_voting:
        print(key, candidates_voting.get(key), sep=' has ')

voting_booth()