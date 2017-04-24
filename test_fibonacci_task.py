# -*- coding: utf-8 -*-
"""

    This file contains Tests for fibonacci_task.py code

    The programm uses the unittest build-in module

"""

from unittest import TestCase, main
import fibonacci_task

class UnitTestCaseFib(TestCase):
    # Error input - negative num
    def test_fn_with_num_neg(self):
        num = -1
        with self.assertRaises(TypeError) as c_m:
            fibonacci_task.fib(num)
        self.assertEqual(c_m.expected, TypeError)
        print(c_m.exception)

    # Error input - num is STRing instead number
    def test_fn_with_num_str(self):
        num = "100"
        with self.assertRaises(TypeError) as c_m:
            fibonacci_task.fib(num)
        self.assertEqual(c_m.expected, TypeError)
        print(c_m.exception)

    # Boundary testing
    def test_fn_with_num_0(self):
        num = 0
        self.assertEqual(0, fibonacci_task.fib(num))

    # Boundary testing
    def test_fn_with_num_1(self):
        num = 1
        self.assertEqual(fibonacci_task.STRPRIME, fibonacci_task.fib(num))

    # Boundary testing
    def test_fn_with_num_2(self):
        num = 2
        self.assertEqual(fibonacci_task.STRPRIME, fibonacci_task.fib(num))

    # F(n) is divisible by 15
    def test_fn_divisible_by_15(self):
        num = 40   # fn = 102334155 = 3 x 5 x 7 x 11 x 41 x 2161
        self.assertEqual(fibonacci_task.STR15, fibonacci_task.fib(num))

    # F(n) is divisible by 5
    def test_fn_divisible_by_5(self):
        num = 55 # fn = 139583862445 = 5 x 89 x 661 x 474541
        self.assertEqual(fibonacci_task.STR5, fibonacci_task.fib(num))

    # F(n) is divisible by 3
    def test_fn_divisible_by_3(self):
        num = 68  # fn = 72723460248141 = 3 x 67 x 1597 x 3571 x 63443
        self.assertEqual(fibonacci_task.STR3, fibonacci_task.fib(num))

    # F(n) is prime
    def test_fn_prime(self):
        num = 83  # fn = 99194853094755497
        self.assertEqual(fibonacci_task.STRPRIME, fibonacci_task.fib(num))

    # F(n) is otherwise than above
    def test_fn_otherwise(self):
        num = 101
        f_n = 573147844013817084101 # 743519377 x 770857978613
        self.assertEqual(f_n, fibonacci_task.fib(num))

    # F(n) is divisible by 15, num=200 is the last big number that is tested
    def test_fn_divisible_by_15_big(self):
        num = 200    # fn = 280571172992510140037611932413038677189525 =
                     #      3 x 5**2 x 7 x 11 x 41 x 101 x 151 x 401 x 2161 x
                     #      3001 x 570601 x 9125201 x 5738108801
        self.assertEqual(fibonacci_task.STR15, fibonacci_task.fib(num))

if __name__ == '__main__':
    main()

