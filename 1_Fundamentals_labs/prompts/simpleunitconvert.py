"""
Tis a file written by Michael
This is known as the 'Unit Converter'
"""

def converter(miles):
    foot = 5280
    feet = miles * foot
    print(feet)

def gather_input():
    miles = int(input('Please enter a number of miles  >>'))
    converter(miles)


gather_input()

# miles = int(input('Please enter a number of miles >>'))
# while True:
# 	if not miles.isdigit():
# 		print("THAT IS NOT A NUMBER!!! TRY AGAIN!!! ")
# 		continue
# 	else:
# 		break
# feet = (miles * foot)

# print(feet)
