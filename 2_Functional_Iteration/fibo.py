"""

>>> fibo(10)
[0, 1, 1, 2, 3, 5, 8]

>>> fibo(20)
[0, 1, 1, 2, 3, 5, 8, 13]

>>> fibo(30)
[0, 1, 1, 2, 3, 5, 8, 13, 21]

"""



# def fibo(ceiling):
#     fibonacci = []
#     former = 0
#     actual = 1
#
#     while actual < ceiling:
#         fibonacci.append(actual)
#         former, actual = actual, former + actual
#
#
#     print(fibonacci)
#
# fibo(10)



def fibo():

    former, actual = 0, 1

    while True:
        yield actual
        former, actual = actual, former + actual



my_gen = fibo()


next(my_gen)
