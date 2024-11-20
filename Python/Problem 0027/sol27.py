"""
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

import math
import time

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_primes(a, b):
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1
    return n

def main():
    max_primes = 0
    max_a = 0
    max_b = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            primes = count_primes(a, b)
            if primes > max_primes:
                max_primes = primes
                max_a = a
                max_b = b
    print(max_a * max_b)

if __name__ == "__main__":
    start = time.time()
    main()
    print("Computation time: ", 1000*(time.time() - start), " ms")