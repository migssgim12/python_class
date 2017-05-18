"""

>>> a = 'music'
>>> b = [17, 28, 42, 31, 12]

>>> display_indexes(a)
m 0
u 1
s 2
i 3
c 4


>>> parallel(a, b)
m 17
u 28
s 42
i 31
c 12

"""

# def display_indexes(a):
#     for index, letter in enumerate(a):
#         print(letter, index)



# def display_indexes(a):
#     for index in range(0, len(a)): # This is taking the index at the first position and the length of the  variable
#         # a,
#         print(a[index], index) # I print each element according to the indexes in the list


def display_indexes(a):
    counter = 0
    while counter < len(a):
        print(a[counter], counter)
        counter += 1



# def parallel(a, b):
#     counter = 0
#     while counter < len(b): # while the counter is less then the length of the list,
#         print(a[counter], b[counter]) # print each element in the string and the list (casting each string into a list)
#         counter += 1


# def parallel(a,b):
#     for a, b in zip(a, b):
#         print(a, b)

# def parallel(a, b):
#     for index, element in enumerate(a): # in the index of the a index, enumerate
#         print(element, b[index]) # get element the b list in each list

# def parallel(a, b):
#     for index in range()



