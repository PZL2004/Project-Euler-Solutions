"""
Evaluate the sum of all the amicable numbers under 10000.
"""
import time

start = time.time()

def sum_proper_divisors(n):
    total = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            total += i
    return total

def sum_amicable_nums(limit):
    total = 0
    checked = []
    for i in range(2, limit): # no need to check 1; not inclusive limit
        a = sum_proper_divisors(i)
        if sum_proper_divisors(a) == i and a != i and i not in checked:
            checked.extend([a, i])
            total += (a+i)
    return total

if __name__ == "__main__":
    print(sum_amicable_nums(10000))
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")