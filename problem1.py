'''
Created on 2013-10-24

@author: oilbeater
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
import timeit

def sol1():
    return sum((i for i in range(1000) if i%3 == 0 or i % 5 == 0))

def sol2():
    threes = sum((i*3 for i in range(1000/3 + 1)))
    fives = sum((i*5 for i in range(1000/5)))
    fifteens = sum((i*15 for i in range(1000/15 + 1)))
    return threes + fives - fifteens
print str(sol1())
print str(sol2())

print timeit.timeit('sol1()',"from __main__ import sol1", number = 10000)
print timeit.timeit('sol2()',"from __main__ import sol2", number = 10000)