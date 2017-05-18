# Lab: Distance Converter

###### Delivery Method: Prompt Only
""" 

--------------

##### Goal

Write a function to convert between `mi`, `km`, `ft`, and `m`.

--------------------

##### Instructions
Ask the user for a distance, then the units of that distance, then the target units.
Then print out the conversion as below.

```
> Enter a distance:
> 100
> Enter units:
> mi
> Enter target units:
> km
> 100 mi is 160.93440000000115 km
```

Support converting between `mi`, `km`, `ft`, and `m`.


-------------------

#### Documentation

1. [Python Official: Built-In Functions](https://docs.python.org/3.6/library/functions.html)

1. [Python Official: Operators](https://docs.python.org/3.6/library/operator.html#mapping-operators-to-functions)

----------------------


## Advanced

*   Also support converting between `in` and `cm`.

*   Also support converting between `gal` and `L`.
    Error if someone tries to convert between volume and distance. Use `raise`.

-------------------


## Super Advanced

* Also support converting between all [metric prefixes](https://en.wikipedia.org/wiki/Metric_prefix) of meters.


------------------------
#### Key Concepts

- Variables
- Function definition
- User input
- Built-In functions
- Logic Problems
1 mile is 1609.344 meters
1 km is 1000 meters
1 foot is .03048 meters

"""

def gather_input():
    question = input('Enter a distance')
    foot = 0.03048
    km = 1000
    mile = 1609.344





























