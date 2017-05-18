
animal = "llama" # assigment of a string to a variable
animal [0]
animal[0:3] # Slicing the sting
animal ='llama'
amz in animal
-False
animal.replace('ll', '$') # Substring Replacement
'$ama'
'{}''.formal(true) # String format syntax
#Type Casting is switching from one to another
animal.upper()
animal.count(l)
2
animal.strip # Removes leading and trailing whitespace

animal.index('a') # Returns position of substring
animal.find('l') #Same thing but doesnt' return an error
list(animal) #Explode - they list all letters of string

animal.replace('l',''$').replace('a','&').lower() # Chaining methods

string.isalpha - # Returns boolean

'{}'.format(True)

phrase = "There once was alady named bright. Who could travel at the speed of light."
words = phrase.replace('.','')'.lower().split()

print(words)
phrase.split('.') # It split removing all periods
phrase.split() # Will split all whitespace
' '.join(words)

import string
String constants where the data is stored in python
string.punctuation
string.ascii_letters
string.digits

phrase = '@#$@#$@#I am @#$#@ the man @#$@'
looping over sting:
    result = '' #initialize and empty string
for char in phrase: # Loop over the phrase
    if (char not in string.punctuation) and (char not in string.digit)
        result = result + char # Add one char at a time if it qualifies

result = phrase.replace(punc, '')
Type casters:
str /
For looping over strings:
Strings are sequences or iterable
you can iterate over a string, list, but not iterate over an integer
for blah in 'kiernan':
    print(blah)
for word in phrase.split():
    print(word)

Lists:
toothpastes = ['Crest','Colgate','Tom\s']
for paste in toothpaste:
    print(paste)
    break

doctesting
python -m doctest knights.py
FUNCTIONS
def a_name(answer):
    result = "Knights who say Ni"
    return result #return is the programatic way and return exits the function
captured = a_name()
captured = a_name()
print(captured)

def simple_search:
toothpastes = ['Crest','Colgate','Tom\s']

max('kiernan')



for paste in toothpaste:
    print(paste)
    break

'llamas'[0:99:0]
'llamas'[::-1] # Alien Smiley, Neg stride.




Loops:
import random
random.randint(0,400__000_000)
planets = ['mars','venus','not pluto']
  for i in planets:
      choice = random.choice(planets)
list(range(10))

for i in range(6):
  choice = random.choice(planets)

  for i in range(int(dice)):
    print
    roll = random.randint(1,6)
