# Problem name: Smallest multiple (problem 5)
# Problem url: https://projecteuler.net/problem=5
# Author: Thorvaldur Gautsson

# Question:

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import functools
import operator

def get_initial_candidate(divisible_by_all_numbers_to):
    return functools.reduce(operator.mul, range(1, divisible_by_all_numbers_to + 1), 1)

def remove_divisors(number, divisible_by_all_numbers_to):
    divisors =  list(reversed([x for x in range(1, divisible_by_all_numbers_to + 1)]))
    for i in range(0, len(divisors)):
        tmp_number = number // divisors[i]
        for y in range(0, len(divisors)):
            if tmp_number % divisors[y] != 0:
                break
            elif y == len(divisors) - 1:
                number = tmp_number
    return number

candidate = get_initial_candidate(20)
print(remove_divisors(candidate, 20))