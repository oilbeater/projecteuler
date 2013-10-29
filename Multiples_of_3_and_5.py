'''
Created on 2013-10-24

@author: oilbeater
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
import timeit


def sol1():
    return sum((i for i in range(1000) if i % 3 == 0 or i % 5 == 0))


def sol2():
    threes = sum((i * 3 for i in range(1000 / 3 + 1)))
    fives = sum((i * 5 for i in range(1000 / 5)))
    fifteens = sum((i * 15 for i in range(1000 / 15 + 1)))
    return threes + fives - fifteens


def sol3():
    threes = (1 + 1000 / 3) * 3 * (1000 / 3) / 2
    fives = (1 + 1000 / 5 - 1) * 5 / 2 * (1000 / 5 - 1)
    fifteens = (1 + 1000 / 15) * 15 * (1000 / 15) / 2
    return threes + fives - fifteens


print str(sol1())
print str(sol2())
print str(sol3())

print timeit.timeit('sol1()', "from __main__ import sol1", number=100000)
print timeit.timeit('sol2()', "from __main__ import sol2", number=100000)
print timeit.timeit('sol3()', "from __main__ import sol3", number=100000)