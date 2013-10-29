'''
Created on 2013-10-29

Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import timeit


def sol1(num):
    sum_of_square = sum(i * i for i in range(1, num + 1))
    square_of_sum = sum(range(1, num + 1)) ** 2
    return square_of_sum - sum_of_square


def sol2(num):
    sum_of_square = (num * (num + 1) / 2) ** 2
    square_of_sum = (2 * num + 1) * (num + 1) * num / 6
    return sum_of_square - square_of_sum


print sol1(100)
print sol2(100)

print timeit.timeit('sol1(100)', "from __main__ import sol1", number=10000)
print timeit.timeit('sol2(100)', "from __main__ import sol2", number=10000)

