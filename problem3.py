'''
Created on 2013-10-28

@author: oilbeater
Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import timeit
from math import sqrt

def findFactors1(num):
    factors = [1]
    for i in range(2,int(sqrt(num)) + 1):
        if num%i == 0:
            factors.append(i)
    factors.append(num)
    return factors

def findFactors2(num):
    factors = [1]
    for i in range(3,int(sqrt(num)) + 1,2):
        if num%i == 0:
            factors.append(i)
    factors.append(num)
    return factors

def isPrime(num):
    for i in range(2,int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    else:
        return True

def sol1(func1,func2):
    factors = func1(600851475143)
    factors.reverse()
    for factor in factors:
        if func2(factor):
            return factor

def sol2(func1,func2):
    factors = func1(600851475143)
    factors.reverse()
    for index, factor in enumerate(factors):
        for subFactor in factors[index + 1:-1]:
            if factor % subFactor == 0:
                break
        else:
            return factor

def sol3(num):
    lastFactor = 1
    if num == 2:
        return 2
    while num % 2 == 0:
        num = num/2
    for factor in range(3,int(sqrt(num)) + 1,2):
        if num < factor:
            break
        while num % factor == 0:
            lastFactor = factor
            num = num/factor
    return lastFactor

print sol1(findFactors1,isPrime)
print sol1(findFactors2,isPrime)
print sol2(findFactors2,isPrime)
print sol3(600851475143)

print timeit.timeit('sol1(findFactors1,isPrime)',"from __main__ import sol1,sol2,isPrime,findFactors2,findFactors1", number = 100)
print timeit.timeit('sol1(findFactors2,isPrime)',"from __main__ import sol1,sol2,isPrime,findFactors2,findFactors1", number = 100)
print timeit.timeit('sol2(findFactors2,isPrime)',"from __main__ import sol1,sol2,isPrime,findFactors2,findFactors1", number = 100)
print timeit.timeit('sol3(600851475143)',"from __main__ import sol3", number = 100)