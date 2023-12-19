"""
There exists exactly one Pythagorean triplet for which a+b+c=1000. Find the product abc.
"""
import time
from math import sqrt

start = time.time()

def prod_pythagorean_trip(n):
    prod = 0
    for a in range(1, n):
        for b in range(a, n):
            c = sqrt(a**2 + b**2)
            if a + b + c == n:
                prod = int(a*b*c)
    return prod


if __name__ == "__main__":
    print(prod_pythagorean_trip(1000)) # if 0 is returned no such pythagorean triple exists such that the sum of them is equal to n
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")