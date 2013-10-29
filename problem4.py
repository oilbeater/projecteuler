'''
Created on 2013-10-28

@author: oilbeater
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import timeit


def is_palindrome(num):
    numstr = str(num)
    if numstr == numstr[::-1]:
        return True
    else:
        return False


def sol1():
    res = 0
    for first in range(999, 99, -1):
        for second in range(first, 99, -1):
            if first * second > res and is_palindrome(first * second):
                res = first * second
    return res


def sol2():
    res = 0
    for first in range(999, 99, -1):
        for second in range(first, 99, -1):
            if first * second < res:
                break
            if is_palindrome(first * second):
                res = first * second
    return res


print sol1()
print sol2()

print timeit.timeit('sol1()', "from __main__ import sol1", number=100)
print timeit.timeit('sol2()', "from __main__ import sol2", number=100)