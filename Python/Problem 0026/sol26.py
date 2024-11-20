"""
Find the value of d<1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

import time

start = time.time()

def get_recurring_cycle_length(n):
    remainders = []
    remainder = 1
    while remainder != 0:
        remainder = remainder * 10 % n
        if remainder in remainders:
            return len(remainders) - remainders.index(remainder)
        remainders.append(remainder)
    return 0

def get_longest_recurring_cycle(limit):
    max_length = 0
    max_d = 0
    for d in range(2, limit):
        length = get_recurring_cycle_length(d)
        if length > max_length:
            max_length = length
            max_d = d
    return max_d

if __name__ == "__main__":
    print(get_longest_recurring_cycle(1000))
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")