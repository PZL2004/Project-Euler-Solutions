"""
What is the largest prime factor of the number 600851475143
"""
from math import sqrt
import time

start = time.time()
    
def max_prime_factor(n):
    #initializing list and first prime number
    a = []
    i = 2
    while i <= n:
        if n % i == 0:
            a.append(i)
            n /= i
        else:
            i += 1

    # max in list will always be last number
    print(a)
    return a[-1]

if __name__ == "__main__":
    print(max_prime_factor(600851475143))
    end = time.time()
    print(f"Compute time {1000*(end-start)} ms")
