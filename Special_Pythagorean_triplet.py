'''
Created on 2013-11-02

@author: oilbeater
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math
import timeit


def sol1(num):
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            if int(math.sqrt(a ** 2 + b ** 2)) ** 2 == a ** 2 + b ** 2 and a + b + math.sqrt(a ** 2 + b ** 2) == num:
                return a * b * int(math.sqrt(a ** 2 + b ** 2))


def sol2(num):
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            if (num - a - b) ** 2 == a ** 2 + b ** 2:
                return a * b * (num - a - b)


print sol1(1000)
print sol2(1000)

print timeit.timeit('sol1(1000)', "from __main__ import sol1", number=10)
print timeit.timeit('sol2(1000)', "from __main__ import sol2", number=10)