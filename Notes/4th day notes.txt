References -
a = 1 # We created a  reference for a place in memory
id(1) = id(a)
b = a
c = b

animal[0]  #access by index
animal[0:3] #start stop and step
if you try to cast the literal to a string it puts everything in quotations
phrase = '@#$@#$@#I am @#$#@ the man @#$@'
looping over sting:

    result = '' #initialize and empty string
for char in phrase: # Loop over the phrase
    if (char not in string.punctuation) and (char not in string.digit)
        result = result + char # Add one char at a time if it qualifies

import random
planets = ['mars','pluto','venus']
for i in range(0,6):
  choice = random.choice(planets)
  print(choice)

  for i in range(0, len(planets)):
      print('Planet #{}'.format(i), planets[i])

      Planet #0 mars
      Planet #1 pluto
      Planet #2 venus

      colors = ['blue','orange', 'white','purple']
      planets = ['mars','pluto','venus','saturn','mercury']
      for i in range(0, len(colors)):
          print(colors[i], planets[i])

          blue mars
          orange pluto
          white venus
          purple saturn
