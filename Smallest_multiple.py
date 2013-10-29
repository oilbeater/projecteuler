'''
Created on 2013-10-29

Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import timeit
import operator


def sol1(nums):
    for index, num in enumerate(nums):
        if num == 1:
            continue
        for bindex, bigger in enumerate(nums[index + 1:]):
            if bigger % num == 0:
                nums[bindex + index + 1] /= num
    result = reduce(operator.mul, nums, 1)
    return result


print sol1(range(1, 21))

print timeit.timeit('sol1(range(1, 21))', "from __main__ import sol1", number=10000)
