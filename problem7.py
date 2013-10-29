'''
Created on 2013-10-29

10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import itertools
from math import sqrt
import timeit


def sol1(nth):
    primes = [2]
    prime_count = 1
    for num in itertools.count(3, 2):
        if prime_count == nth:
            return primes[-1]
        for prime in primes:
            if num % prime == 0:
                break
        else:
            primes.append(num)
            prime_count += 1


def sol2(nth):
    primes = [2]
    prime_count = 1
    for num in itertools.count(3, 2):
        if prime_count == nth:
            return primes[-1]
        for prime in primes:
            if num % prime == 0:
                break
            if prime > sqrt(num):
                primes.append(num)
                prime_count += 1
                break


print sol1(10001)
print sol2(10001)

print timeit.timeit('sol1(10001)', "from __main__ import sol1", number=1)
print timeit.timeit('sol2(10001)', "from __main__ import sol2", number=1)