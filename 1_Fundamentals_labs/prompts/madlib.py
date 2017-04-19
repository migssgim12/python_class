"""
This is a file written by Michael
This is known as the 'Module level docstring'
"""


def gather_input(age):
	name = input('What is your name?  >>')
	nounPlur = input('Give me a plural noun >>')
	place =input('Give me a place  >>')
	noun = input('Noun >>')
	nounPlur2 = input('Another plural noun >>')
	noun2 = input('Noun >>')
	adjective = input('adjective  >>')
	verb = input('verb >>')
	number = input('number >>')
	adjective2 = input('adjective >>')
	bodyPart = input('body part >>')
	verb2 =input('verb >>')

	print('Hello {name}, you are {age} years old. You are going to edit Shakespeares work! Here we go. '' Two {nounPlur}, both alike in dignity\n (In fair {place}, where we lay our scene),\n From ancient {noun} break to new mutiny,\n Where civil blood makes civil hands unclean./n From forth the fatal loins of these two foes \n A pair of star-crossed {nounPlur2} take their life,\n Do with their {noun2} bury their parents strife.\n The fearful passage of their {adjective} love \n And the continuance of their parents\' rage, /n Which, but their children’s end, \n naught could {verb}, \n Is now the {number} hours traffic of our stage—The which, \n if you with {adjective2} {bodyPart} attend, \n What here shall {verb2} \n our toil shall strive to mend.'.format(age=age,name=name,nounPlur=nounPlur,place=place,noun=noun,nounPlur2=nounPlur2,noun2=noun2,adjective=adjective,verb=verb,number=number,adjective2=adjective2,bodyPart=bodyPart,verb2=verb2))


def conditions():
	while True:
		try:
			age = int(input('What is your age?  >> '))
		except ValueError:
			print("THAT IS NOT A NUMBER!!! TRY AGAIN!!! ")
			continue
		if age < 18:
			print("You are not old enough to play ")
			quit()
		else:
			print("Ok you are old enough to play")
			gather_input(age)
			break

conditions()
