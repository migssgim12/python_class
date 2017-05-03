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
    # candidate_choices.update({len(candidate_choices)+1: 'leave now.'})

    while True:
        list_of_candidates()
        prompt = input('>>  ')
        try:
            prompt = int(prompt)
            choice = candidate_choices[prompt]
            candidates_voting[choice] += 1
            for key in candidates_voting:
                print(key, candidates_voting.get(key), sep=' has ')
            continue
        except ValueError:
            if prompt == 'done':
                for key in candidates_voting:
                    print(key, candidates_voting.get(key), sep=' has ')
                break
            elif prompt =='list':
                print('These are the tallies so far: ')
                for key in candidates_voting:
                    print(key, candidates_voting.get(key), sep=' has ')
                continue
            print('Please enter a valid number')
            continue


def list_of_candidates():
    for index, element in enumerate(candidates, start=1):
        print('Press', index, 'for', element)
    print("Enter 'done' to quit, or 'list' to list the tallies")

    # print(index+1, 'leave now')




voting_booth()