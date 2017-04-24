# -*- coding: utf-8 -*-
"""
       This module This module has been created as part of submitting
       my application form for Software, Product, and
       Embedded Engineering Candidates

"""

import math

# Return string definition values
STR3 = "Buzz"
STR5 = "Fizz"
STR15 = "FizzBuzz"
STRPRIME = "BuzzFizz"

def fib(num):
    """
        Generate the first 'n' Fibonacci numbers F(n) and print the required
        return values

        Args:
            n: int - num >=0

        Returns:
             string "Buzz": when F(n) is divisible by 3.
             string "Fizz": when F(n) is divisible by 5.
             string "FizzBuzz": when F(n) is divisible by 15.
             string "BuzzFizz": when F(n) is prime.
             F(n): int otherwise.

        Raises:
            ValueError: If num <= 0 or num is string

        Warning:
            This function has been tested with the maximum 'num' value
            is equal to 200

        Note:
            This function uses the iterative version to calculate Fibonacci numbers.
            It is a lot faster than the recursive version.

    """
    try:
        if isinstance(num, int) is False:
            raise TypeError("Error input num - Not number", num)
        if num < 0:
            raise TypeError("Error input num - Negative", num)
        # num is Ok
        if num == 0:           # special case
            return 0
        # Initial values
        f_1, f_2 = 0, 1
        for _ in range(num):
            f_1, f_2 = f_2, f_1 + f_2
        # Return values accordig to req
        if f_1 %15 == 0:
            return STR15
        elif f_1 %5 == 0:
            return STR5
        elif f_1 %3 == 0:
            return STR3
        elif help_is_prime(f_1):
            return STRPRIME
        else:
            return f_1
    except TypeError as err:
        raise err

def help_is_prime(num):
    """
        Check if the given number is prime or not

        Args:
             n: int - the input number

        Returns:
             True    - if the input numer is prime
             False   - otherwise

        Note:
             This function uses Sieve of Eratosthenes algorithm.
             It only checks up to the floor of the square root of the number.
             The time complexity of calculating all primes below n
             in the random access machine model is O(n log log n) operations

    """
    for j in range(2, int(math.sqrt(num))):
        if (num % j) == 0:
            return False
    return True
