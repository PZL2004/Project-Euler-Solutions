"""
Find the sum of the digits in the number 100!.
"""
import time
from math import factorial

start = time.time()

def sum_of_digits_factorial(n):
    fac = str(factorial(n))
    return sum(int(x) for x in fac)

if __name__ == "__main__":
    print(sum_of_digits_factorial(100))
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")