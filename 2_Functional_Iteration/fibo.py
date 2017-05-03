"""

>>> fibo(10)
[0, 1, 1, 2, 3, 5, 8]

>>> fibo(20)
[0, 1, 1, 2, 3, 5, 8, 13]

>>> fibo(30)
[0, 1, 1, 2, 3, 5, 8, 13, 21]

"""



def fibo(ceiling):
    fibonacci = []
    former = 0
    actual = 1

    while former < ceiling:
        fibonacci.append(former)
        former, actual = actual, former + actual


    return fibonacci


