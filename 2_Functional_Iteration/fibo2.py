def fibo(ceiling):
    fibonacci = []
    former = 0
    actual = 1

    while former < ceiling:
        fibonacci.append(former)
        former, actual = actual, former + actual


    return fibonacci


fibo(10)
