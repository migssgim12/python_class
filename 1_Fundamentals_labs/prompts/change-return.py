"""
Change return
"""



def coin_return():
	cents = int(input('How much money do you have?  >>'))
	# cents = int(input('How much change do you need in cents?  >>'))
	hundreds = cents //100 
	quarters = cents // 25 
	cents_left = cents -(quarters * 25)
	dimes = cents_left // 10
	cents_left = cents_left - (dimes *10)
	nickles = cents_left //5
	cents_left =cents_left -(nickles *5)
	pennies = cents_left //1
	print('You have ', quarters, 'quarters')
	print('You have ', dimes, 'dimes')
	print('You have ', nickles, 'nickles')
	print('You have ', pennies, 'pennies')


# cents = int(input('How much change do you need in cents?  >>'))

coin_return()

# divmod('96,25')

