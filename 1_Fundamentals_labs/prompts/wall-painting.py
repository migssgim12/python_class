"""
Tis a file written by Michael
This is known as the 'wall-painting'
I am finding how much it will cost to paint a w

"""
import math



def gather_input():
	width = int(input("What is the width of your wall >>"))
	height = int(input("what is the Height  >>"))
	coats = int(input("How many coats  >>"))
	calculate(width, height, coats)

def calculate(width, height, coats):
	gallon_price = 10
	gallon_covers = 400
	area = width * height
	paint_price = area / 400 * gallon_price * coats
	print('Your wall will cost:  {0:.2f} dollars'.format(paint_price))
	gallons = paint_price / gallon_price
	gallons_round_up = math.ceil(gallons)
	print('You will need at least {} gallons'.format(gallons_round_up))

gather_input()
